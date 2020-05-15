#test to determine maximum sample rate of ina219 via raspberry pi

import time
import sys
import board
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219, Mode
import datetime
import numpy as np
import pandas as pd
import csv

global_flag = True


def recordEnergyConsumption(path='data'):
    print("ina219 start")
    fileName = path+'/ina219-'+str(datetime.date.today())+'-'+str(int(time.time()))+'.csv'

    i2c_bus = board.I2C()
    ina219 = INA219(i2c_bus)

    # optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
    ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_128S
    ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_128S
    # optional : change voltage range to 16V
    ina219.bus_voltage_range = BusVoltageRange.RANGE_16V

    ina219.mode = Mode.SVOLT_CONTINUOUS


    dataDF = pd.DataFrame(columns=['mA','V','time'])

    startTime = time.time()

    #run till selenium done
    while global_flag:
        if ina219.conversion_ready == 1:
            bus_voltage = ina219.bus_voltage        # voltage on V- (load side)
            current = ina219.current                # current in mA            
            dataDF = dataDF.append({'mA' : current , 'V' : bus_voltage, 'time': time.time()},ignore_index=True)

    elapsedTime = time.time()
    testTime = elapsedTime - startTime

    #save data to file
    try:
        with open(fileName) as csvfile:
            print("This file already exists!")
    except:
        dataDF.to_csv(fileName, sep=',',index=False)
    
    print("ina219 done")

if __name__ == "__main__":
    recordEnergyConsumption()