"""Sample code and test for adafruit_in219"""

from time import sleep
import datetime
import os
import json
import collections as cl
import board
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219


def json_serial(obj):
    if isinstance(obj, (datetime.datetime)):
        return obj.isoformat()
    
def append_json_to_file(data: dict, path_file: str) -> bool:
    with open(path_file, 'ab+') as f:
        f.seek(0,2)
        if f.tell() == 0:
            f.write(json.dumps([data], default=json_serial).encode())
        else :
            f.seek(-1,2)
            f.truncate()
            f.write(' , '.encode())
            f.write(json.dumps(data, default=json_serial).encode())
            f.write(']'.encode())
    return f.close()


i2c_bus = board.I2C()
ina219 = INA219(i2c_bus)

# display some of the advanced field (just to test)
print("Config register:")
print("  bus_voltage_range:    0x%1X" % ina219.bus_voltage_range)
print("  gain:                 0x%1X" % ina219.gain)
print("  bus_adc_resolution:   0x%1X" % ina219.bus_adc_resolution)
print("  shunt_adc_resolution: 0x%1X" % ina219.shunt_adc_resolution)
print("  mode:                 0x%1X" % ina219.mode)
print("")

# optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
# optional : change voltage range to 16V
ina219.bus_voltage_range = BusVoltageRange.RANGE_16V

# measure and display loop
while True:

    fileName = 'data/ina219_'+str(datetime.date.today())+'.json'

    bus_voltage = ina219.bus_voltage        # voltage on V- (load side)
    shunt_voltage = ina219.shunt_voltage    # voltage between V+ and V- across the shunt
    psu_voltage = bus_voltage + shunt_voltage
    current = ina219.current/1000           # current in A
    power = ina219.power

    # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
    print("Datetime: ", datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    print("PSU Voltage: {:6.3f} V".format(psu_voltage))
    print("Shunt Voltage: {:9.6f} V".format(shunt_voltage))
    print("Bus Voltage: {:6.3f} V".format(bus_voltage))
    print("Current: {:9.6f} A".format(current))
    print("Power: {:9.6f} W".format(power))
    print("")

    data = {
        "datetime" : datetime.datetime.now(),
        "psu_voltage" : psu_voltage,
        "shunt_voltage" : shunt_voltage,
        "bus_voltage" : bus_voltage,
        "current" : current,
        "power" : power,
    }

    append_json_to_file(data, fileName)

    sleep(60)
