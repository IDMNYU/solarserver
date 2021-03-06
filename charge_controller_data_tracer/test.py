# pymodbus code based on the example from http://www.solarpoweredhome.co.uk/

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from time import sleep
import datetime
import numpy as np
import pandas as pd
import csv
import os

client = ModbusClient(method = 'rtu', port = '/dev/ttyUSB0', baudrate = 115200)
client.connect()

while True:
    #doesn't need to happen every time, just at midnight
    #fileName = '/home/pi/Desktop/EPSolar_Tracer/data/tracerData'+str(datetime.date.today())+'.csv' 

    result = client.read_input_registers(0x3100,16,unit=1)

    solarVoltage = float(result.registers[0] / 100.0)
    solarCurrent = float(result.registers[1] / 100.0)
    solarPowerL = float(result.registers[2] / 100.0)
    solarPowerH = float(result.registers[3] / 100.0)
    
    print("solarVoltage: " + str(solarVoltage))
    print("solarCurrent: " + str(solarCurrent))
    print("solarPowerL: " + str(solarPowerL))
    print("solarPowerH: " + str(solarPowerH))
    print()
    
    batteryVoltage = float(result.registers[4] / 100.0)
    battetyChargingCurrent = float(result.registers[5] / 100.0)
    battetyChargingPowerL = float(result.registers[6] / 100.0)
    battetyChargingPowerH = float(result.registers[7] / 100.0)
    
    print("batteryVoltage: " + str(batteryVoltage))
    print("battetyChargingCurrent: " + str(battetyChargingCurrent))
    print("battetyChargingPowerL: " + str(battetyChargingPowerL))
    print("battetyChargingPowerH: " + str(battetyChargingPowerH))
    print()

    loadVoltage = float(result.registers[8] / 100.0)
    loadCurrent = float(result.registers[9] / 100.0)
    loadPowerL = float(result.registers[10] / 100.0)
    loadPowerH = float(result.registers[11] / 100.0)
    
    print("loadVoltage: " + str(loadVoltage))
    print("loadCurrent: " + str(loadCurrent))
    print("loadPowerL: " + str(loadPowerL))
    print("loadPowerH: " + str(loadPowerH))
    print()

    sleep(1)


    """
    batteryVoltage = float(result.registers[4] / 100.0)
    chargeCurrent = float(result.registers[5] / 100.0)
    chargePowerL = float(result.registers[6] / 100.0)
    chargePowerH = float(result.registers[7] / 100.0)
    loadVoltage = float(result.registers[8] / 100.0)
    loadCurrent= float(result.registers[9] / 100.0)
    loadPower= float(result.registers[10] / 100.0)

    result = client.read_input_registers(0x311A,2,unit=1)
    batteryPercentage = float(result.registers[0] / 100.0)

    dateTimeNow = datetime.datetime.now()
    currentTime = dateTimeNow.time()
    currentDate = datetime.date.today() #updated but not pushed - check that it is correct and works

    # Do something with the data
    '''
    print("PV Voltage: " + str(solarVoltage))

    print("PV Current" + str(solarCurrent))

    print("Battery Voltage: " + str(batteryVoltage))

    print("Charge Current: " + str(chargeCurrent))
    print("Load Current" + str(loadCurrent))
    print("Load Power: " + str(loadPower))
    
    print("Local time: " + str(currentDate))
    '''

    newDF = pd.DataFrame(data={
        "PV voltage": [solarVoltage],
        "PV current": [solarCurrent],
        "PV power L": [solarPowerL],
        "PV power H": [solarPowerH],
        "battery voltage":[batteryVoltage],
        "charge current":[chargeCurrent],
        "charge power L":[chargePowerL],
        "charge power H": [chargePowerH],
        "load voltage":[loadVoltage],
        "load current": [loadCurrent],
        "load power": [loadPower],
        "battery percentage": [batteryPercentage],
        "time": [currentTime],
        "date" : [currentDate]})

    # check if the file already exists
    try:
        with open(fileName) as csvfile:
            df = pd.read_csv(fileName)
            print(df)
            df = df.append(newDF, ignore_index = True)
            df.to_csv(fileName, sep=',',index=False)
            #print("It exists!")
    except:
        print("first file of the day!")
        newDF.to_csv(fileName, sep=',',index=False)

    #runs every minute
    sleep(60)
    """

client.close()