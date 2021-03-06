import threading
import ina219_datarecorder
import imagesize_pingpong
import aggregator
import os
import time
import datetime

folderName = str(datetime.date.today())+'-'+str(int(time.time()))
newDirPath = 'data/'+ folderName
os.mkdir(newDirPath)

thread1 = threading.Thread(target=ina219_datarecorder.recordEnergyConsumption, args=([newDirPath]))
thread2 = threading.Thread(target=imagesize_pingpong.pingpongImage, args=([newDirPath]))
thread1.start()
thread2.start()
thread2.join()
ina219_datarecorder.global_flag = False
thread1.join()

print("Run aggregator")
aggregator.aggregate(newDirPath)