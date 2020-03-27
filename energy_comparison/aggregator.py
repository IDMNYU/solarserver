import csv
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import time
import datetime
import glob
import matplotlib.patches as mpatches
import sys
import math


def readCSV(fileList):
    inaFileName = [k for k in fileList if 'ina' in k]
    inaData = pd.read_csv(inaFileName[0], dtype={"time": float})
    #print(inaData.shape)
    #print(inaData.head())
    return inaData

# add power to inaData
def addWatts(inaData):
    inaData.insert(2, 'watts', (inaData.mA / 1000.0) * inaData.V, True)
    #print(inaData.shape)
    #print(inaData.head())
    return inaData

def readSelemium(fileList):
    selFileName = [k for k in fileList if 'selenium' in k]
    selRawData = pd.read_csv(selFileName[0], dtype={"time": float})
    #print(selRawData.shape)
    #print(selRawData.head())
    return selRawData

def organizeSeleniumData(inaData, selRawData):
    selVolts = []
    selCurrents = []
    selWatts = []
    selTimes = []
    taskTypes = []

    for taskType, selTime in zip(selRawData.task, selRawData.time):
        for inaVolt, inaCurrent, inaWatt, inaTime in zip(inaData.V, inaData.mA, inaData.watts, inaData.time):
            if math.isclose(selTime, inaTime, rel_tol=0.000000001):
                taskTypes.append(taskType)
                selTimes.append(inaTime)
                selWatts.append(inaWatt)
                selVolts.append(inaVolt)
                selCurrents.append(inaCurrent)

    return pd.DataFrame({"volts": selVolts, "currents": selCurrents, "watts": selWatts, "time": selTimes, "task": taskTypes})

def drawWattGraph(inaData, selData, colors):
    inaData.plot(x='time', y='watts', linewidth = 0.5)
    plt.scatter(x=selData.time, y=selData.watts, c=selData.task.str[0].apply(lambda x: colors[x]))
    plt.savefig('watts.png')
    #plt.show()

def drawVoltGraph(inaData, selData, colors):
    inaData.plot(x='time', y='V', linewidth = 0.5)
    plt.scatter(x=selData.time, y=selData.volts, c=selData.task.str[0].apply(lambda x: colors[x]))
    plt.savefig('volts.png')
    #plt.show()

def drawCurrentGraph(inaData, selData, colors):
    inaData.plot(x='time', y='mA', linewidth = 0.5)
    plt.scatter(x=selData.time, y=selData.currents, c=selData.task.str[0].apply(lambda x: colors[x]))
    plt.savefig('currents.png')
    #plt.show()

def aggregate(path='data'):
    dirPath = path + "/"
    fileList = glob.glob(dirPath + "*.csv")

    # read ina.csv file add a new column of wattage
    inaData = readCSV(fileList)
    inaData = addWatts(inaData)

    # read selenium csv file and organize data
    selRawData = readSelemium(fileList)
    selData = organizeSeleniumData(inaData, selRawData)

    # graph
    colors = {'0':'red', '1':'blue'} # TODO: automate

    drawWattGraph(inaData, selData, colors)
    drawVoltGraph(inaData, selData, colors)
    drawCurrentGraph(inaData, selData, colors)


if __name__ == "__main__":
    aggregate()