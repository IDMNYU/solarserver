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

def wattComparison(inaData, selRawData):
    selWatts = []
    selTimes = []
    for selTime in selRawData.time:
        for inaWatt, inaTime in zip(inaData.watts, inaData.time):
            if math.isclose(selTime, inaTime, rel_tol=0.000000001):
                print("sel: " + str(selTime))
                print("ina: " + str(inaTime))
                print(inaWatt)
                selTimes.append(inaTime)
                selWatts.append(inaWatt)

    selData = pd.DataFrame({"watts": selWatts, "time": selTimes})
    print(selData.head())

    # graph
    inaData.plot(x='time', y='watts', linewidth = 0.5)
    plt.scatter(x=selData.time, y=selData.watts, c='red')
    #plt.show()
    plt.savefig('watts.png')

def voltageComparison(inaData, selRawData):
    selVolts = []
    selTimes = []
    for selTime in selRawData.time:
        for inaVolt, inaTime in zip(inaData.V, inaData.time):
            if math.isclose(selTime, inaTime, rel_tol=0.000000001):
                print("sel: " + str(selTime))
                print("ina: " + str(inaTime))
                print(inaVolt)
                selTimes.append(inaTime)
                selVolts.append(inaVolt)

    selData = pd.DataFrame({"volts": selVolts, "time": selTimes})
    print(selData.head())

    # graph
    inaData.plot(x='time', y='V', linewidth = 0.5)
    plt.scatter(x=selData.time, y=selData.volts, c='red')
    #plt.show()
    plt.savefig('volts.png')

def currentComparison(inaData, selRawData):
    selCurrents = []
    selTimes = []
    for selTime in selRawData.time:
        for inaCurrent, inaTime in zip(inaData.mA, inaData.time):
            if math.isclose(selTime, inaTime, rel_tol=0.000000001):
                print("sel: " + str(selTime))
                print("ina: " + str(inaTime))
                print(inaCurrent)
                selTimes.append(inaTime)
                selCurrents.append(inaCurrent)

    selData = pd.DataFrame({"currents": selCurrents, "time": selTimes})
    print(selData.head())

    # graph
    inaData.plot(x='time', y='mA', linewidth = 0.5)
    plt.scatter(x=selData.time, y=selData.currents, c='red')
    #plt.show()
    plt.savefig('currents.png')


# In[2]:
def aggregate(path=""):
    #testDirPath = path + "/"
    #fileList = glob.glob(testDirPath + "*.csv")
    fileList = glob.glob("*.csv")

    # read ina.csv file add a new column of wattage
    inaData = readCSV(fileList)
    inaData = addWatts(inaData)

    # read selenium csv file
    selRawData = readSelemium(fileList)

    # save a png comparing watts/volts/currents between large and small images
    # depends on timeframe of ina and selenium data
    #wattComparison(inaData, selRawData)
    #voltageComparison(inaData, selRawData)
    #currentComparison(inaData, selRawData)


    """
    # In[10]:
    #averages per second
    inaLength = inaData.shape[0]
    inaStartTime = inaData.time[0]
    inaEndTime = inaData.time[inaData.shape[0]-1]
    inaTimePeriod = inaEndTime - inaStartTime
    dataPerSecond =inaLength/inaTimePeriod




    # In[11]:
    averagedINA = pd.DataFrame(columns=['mA','V','watts','time'])

    for av in list(range(int(inaTimePeriod))):
        avmA= inaData.loc[(15*av):((15*av)+14)]['mA'].sum()/15
        avV = inaData.loc[(15*av):((15*av)+14)]['V'].sum()/15
        avWatts = inaData.loc[(15*av):((15*av)+14)]['watts'].sum()/15
        avTime = inaData.loc[(15*av):(15*av)]['time'][inaData.loc[(15*av):(15*av)]['time'].index[0]]
        averagedINA = averagedINA.append({'mA' : avmA , 'V' : avV, 'watts': avWatts,'time': avTime},ignore_index=True)

        


    # In[12]:
    print(averagedINA.shape)
    print(averagedINA.tail())


    # In[13]:
    seleniumData = pd.read_csv(selFileName[0]).fillna(0)


    # In[14]:
    print(seleniumData.shape)
    seleniumData.tail()


    # In[15]:
    seleniumData.task.loc[0]


    # In[16]:
    # get start and stop times
    testTimes = []

    currentRound = 0
    for getT in list(range(seleniumData.shape[0])):
        
        if 'start' in seleniumData.task.loc[getT]:
            roundTimes = [seleniumData.time.loc[getT]]
        elif 'stop' in seleniumData.task.loc[getT]:
            roundTimes.append(seleniumData.time.loc[getT])
            testTimes.append(roundTimes)

    # In[17]:
    #make new data frames with power data from only test durations
    dataFrameSplits = []

    #print(averagedINA)
    for splitTests in list(range(len(testTimes))):
        dataFrameSplits.append(averagedINA.loc[(averagedINA.loc[:,'time']>=(testTimes[splitTests][0])) & (averagedINA.loc[:,'time']<=testTimes[splitTests][1])])
        #print(dataFrameSplits[splitTests])
        #print(averagedINA.loc[(averagedINA.loc[:,'time']>=(testTimes[splitTests][0])) & (averagedINA.loc[:,'time']<=testTimes[splitTests][1])])
    print(len(dataFrameSplits))



    # In[18]:
    #get the max and mins for each test set
    for mX in list(range(len(dataFrameSplits))):
        print('------'+str(mX)+'------')
        print ('Max:')
        print (np.max(dataFrameSplits[mX].watts))
        print ('Min:')
        print (np.min(dataFrameSplits[mX].watts))
                


    # In[19]:
    #obviously this isn't automated...
    #large average peak
    lPeakAVG =(2.6139504000000002 + 2.596789200000001 + 2.5888593333333336 + 2.6099552000000004) * 0.25

    #small overall peak
    sPeakAVG =(2.294001466666667+2.293759333333334+2.2986020000000003+2.2974821333333337)* 0.25

    print("Large Peak AVG: " + str(lPeakAVG))
    print("Small Peak AVG: " + str(sPeakAVG))

    #peak differences
    print("AVG Peak Difference: " + str(lPeakAVG-sPeakAVG))


    # In[20]:
    #graph ina219 all data
    plt.scatter(x=inaData.loc[:,'time'], y=inaData.loc[:,'watts'], color='b')


    # In[21]:
    # graph all selenium data
    plt.scatter(x=seleniumData.loc[:,'time'], y=seleniumData.loc[:,'task'], color='b')


    # In[22]:
    fig, ax = plt.subplots(dpi=300)

    x = averagedINA.loc[:,'time']
    y = averagedINA.loc[:,'V']
    ax.plot(x,y)

    ax.set(xlabel='seconds', ylabel='volts',
           title='Server Activity')

    colors = ['r','y','b','g']
    for plotNum in list(range(len(dataFrameSplits))):
        ax.scatter(x=dataFrameSplits[plotNum].loc[:,'time'], y=dataFrameSplits[plotNum].loc[:,'V'], color=colors[plotNum%2])

    redLabel = mpatches.Patch(color='red', label='large')
    blueLabel = mpatches.Patch(color='blue', label='small')
    yellowLabel = mpatches.Patch(color='yellow', label='small')
    greenLabel = mpatches.Patch(color='green', label='small image')


    plt.legend(handles=[redLabel, yellowLabel])

    #ax.grid()
    pngName1 = testDirectoryPath +"voltage_"+str(datetime.date.today())+"-"+str(int(time.time()))+".png"
    print(pngName1)
    fig.savefig(pngName1)
    plt.show()


    # In[23]:
    fig, ax = plt.subplots(dpi=300)

    x = averagedINA.loc[:,'time']
    y = averagedINA.loc[:,'mA']
    ax.plot(x,y)

    ax.set(xlabel='seconds', ylabel='mA',
           title='Server Activity')

    colors = ['r','y','b','g']
    for plotNum in list(range(len(dataFrameSplits))):
        ax.scatter(x=dataFrameSplits[plotNum].loc[:,'time'], y=dataFrameSplits[plotNum].loc[:,'mA'], color=colors[plotNum%2])

    redLabel = mpatches.Patch(color='red', label='large')
    blueLabel = mpatches.Patch(color='blue', label='large image')
    yellowLabel = mpatches.Patch(color='yellow', label='small')
    greenLabel = mpatches.Patch(color='green', label='small image')

    plt.legend(handles=[redLabel, yellowLabel])

    #ax.grid()
    pngName1 = testDirectoryPath +"current_"+str(datetime.date.today())+"-"+str(int(time.time()))+".png"
    print(pngName1)
    fig.savefig(pngName1)
    plt.show()


    # In[24]:
    fig, ax = plt.subplots(dpi=300)

    x = averagedINA.loc[:,'time']
    y = averagedINA.loc[:,'watts']
    ax.plot(x,y)

    ax.set(xlabel='seconds', ylabel='watts',
           title='Server Activity')

    colors = ['r','y','b','g']
    for plotNum in list(range(len(dataFrameSplits))):
        ax.scatter(x=dataFrameSplits[plotNum].loc[:,'time'], y=dataFrameSplits[plotNum].loc[:,'watts'], color=colors[plotNum%2])

    redLabel = mpatches.Patch(color='red', label='large')
    blueLabel = mpatches.Patch(color='blue', label='large image')
    yellowLabel = mpatches.Patch(color='yellow', label='small')
    greenLabel = mpatches.Patch(color='green', label='small image')

    plt.legend(handles=[redLabel, yellowLabel])

    #ax.grid()
    pngName1 = testDirectoryPath +"watts_"+str(datetime.date.today())+"-"+str(int(time.time()))+".png"
    print(pngName1)
    fig.savefig(pngName1)
    plt.show()


    # In[25]:
    overlayData = dataFrameSplits
    overlayData[2]


    # In[26]:
    list(range(len(dataFrameSplits)))


    # In[27]:
    overlayData[0]


    # In[28]:
    for overlays in list(range(len(dataFrameSplits))):
        overlayData[overlays].insert(4, 'scaled', overlayData[overlays].time - overlayData[overlays].time[overlayData[overlays].time.index[0]], True)

    #overlayData


    # In[29]:
    fig, ax = plt.subplots(dpi=300)
    '''
    x = overlayD1.loc[:,'scaled']
    y = overlayD1.loc[:,'watts']
    ax.plot(x,y, color='r')

    ax.set(xlabel='time', ylabel='watts',
           title='Overlayed Server Activity')

    '''

    colors = ['r','y','b','g']
    for plotNum in list(range(len(overlayData))):
        ax.plot(overlayData[plotNum].loc[:,'scaled'], overlayData[plotNum].loc[:,'watts'], color=colors[plotNum%2])

    ax.set(xlabel='seconds', ylabel='watts',
           title='Overlayed Server Activity')

    redLabel = mpatches.Patch(color='red', label='large')
    blueLabel = mpatches.Patch(color='blue', label='large image')
    yellowLabel = mpatches.Patch(color='yellow', label='small')
    greenLabel = mpatches.Patch(color='green', label='small image')

    plt.legend(handles=[redLabel, yellowLabel])

    #ax.grid()
    pngName2 = testDirectoryPath +"aggregator_overlay-"+str(datetime.date.today())+"-"+str(int(time.time()))+".png"
    print(pngName2)
    fig.savefig(pngName2)
    plt.show()
    """

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        aggregate(str(sys.argv[1]))
    else:
        #print("Error: no folder name given.")
        #sys.exit()
        aggregate()