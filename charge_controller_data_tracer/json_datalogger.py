# pymodbus code based on the example from http://www.solarpoweredhome.co.uk/

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from time import sleep
import datetime
import os
import json
import collections as cl

def json_serial(obj):
    if isinstance(obj, (datetime.datetime)):
        return obj.isoformat()
    
def append_json_to_file(data: dict, path_file: str) -> bool:
    with open(path_file, 'ab+') as f:              # ファイルを開く
        f.seek(0,2)                                # ファイルの末尾（2）に移動（フォフセット0）  
        if f.tell() == 0 :                         # ファイルが空かチェック
            print("first file of the day!")
            f.write(json.dumps([data], default=json_serial).encode())   # 空の場合は JSON 配列を書き込む
        else :
            f.seek(-1,2)                           # ファイルの末尾（2）から -1 文字移動
            f.truncate()                           # 最後の文字を削除し、JSON 配列を開ける（]の削除）
            f.write(' , '.encode())                # 配列のセパレーターを書き込む
            f.write(json.dumps(data, default=json_serial).encode())     # 辞書を JSON 形式でダンプ書き込み
            f.write(']'.encode())                  # JSON 配列を閉じる
    return f.close() # 連続で追加する場合は都度 Open, Close しない方がいいかも


client = ModbusClient(method = 'rtu', port = '/dev/ttyUSB0', baudrate = 115200)
client.connect()

while True:
    #doesn't need to happen every time, just at midnight
    fileName = 'data/tracerData'+str(datetime.date.today())+'.json' 

    result = client.read_input_registers(0x3100,16,unit=1)
    solarVoltage = float(result.registers[0] / 100.0)
    solarCurrent = float(result.registers[1] / 100.0)
    solarPower = float(result.registers[2] / 100.0)

    batteryVoltage = float(result.registers[4] / 100.0)
    battetyCurrent = float(result.registers[5] / 100.0)
    battetyPower = float(result.registers[6] / 100.0)

    loadVoltage = float(result.registers[8] / 100.0)
    loadCurrent = float(result.registers[9] / 100.0)
    loadPower = float(result.registers[10] / 100.0)

    result = client.read_input_registers(0x311A,2,unit=1)
    batteryPercentage = float(result.registers[0] / 100.0)

    data = {
        "date" : datetime.datetime.now(),
        "solarVoltage" : solarVoltage,
        "solarCurrent" : solarCurrent,
        "solarPower" : solarPower,
        "batteryVoltage" : batteryVoltage,
        "battetyCurrent" : battetyCurrent,
        "battetyPower" : battetyPower,
        "loadVoltage" : loadVoltage,
        "loadCurrent" : loadCurrent,
        "loadPower" : loadPower,
        "batteryPercentage" : batteryPercentage,
    }
    
    #jsonData = json.dumps(data, default=json_serial)
    #print(jsonData)

    append_json_to_file(data, fileName)

    #runs every 5sec
    sleep(5)

client.close()