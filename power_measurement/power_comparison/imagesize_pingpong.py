#example from https://selenium-python.readthedocs.io/getting-started.html

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
import time
import datetime
import numpy as np
import pandas as pd
import csv
import sys


class SolarServerTest:
    
    def __init__(self):
        #need to avoid cache for accurate tests in some instances
        self.profile = webdriver.firefox.firefox_profile.FirefoxProfile()
        self.profile.set_preference("browser.cache.disk.enable", False)
        self.profile.set_preference("browser.cache.memory.enable", False)
        self.profile.set_preference("browser.cache.offline.enable", False)
        self.profile.set_preference("network.http.use-cache", False)
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options, firefox_profile=self.profile)
        
    def test_click(self, url):

        self.driver.get(url)

        assert "dropdown" in self.driver.title
        
        menu = self.driver.find_element_by_class_name("dropbtn")
        hidden_submenu = self.driver.find_element_by_id("submenu1")

        actions = ActionChains(self.driver)
        actions.move_to_element(menu)
        actions.click(hidden_submenu)
       
        actions.perform()

        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.close()
        #self.driver.quit()

def pingpongImage(path='data'):
    print("pingpong start")
    
    SERVER_IP = ""
    if (len(sys.argv) > 1):
        SERVER_IP = str(sys.argv[1])
    else:
        print("Error: no ip address given.")
        sys.exit()

    fileName = path+'/selenium-'+str(datetime.date.today())+'-'+str(int(time.time()))+'.csv' 

    dataDF = pd.DataFrame(columns=['task','time'])

    testTime = 5
    bookendSleepTime = 60
    middleSleepTime = 30

    #60 seconds idle for the beggining
    time.sleep(bookendSleepTime)

    #open
    times = 3

    # run the whole thing i times to account for start up weirdness
    for i in list(range(times)):
        #Phase 1
        print ("Starting large test!")

        dataDF = dataDF.append({'task' : '0_' + str(i) + '_start', 'time': time.time()},ignore_index=True)
        SolarServer = SolarServerTest()

        tmCurrentTime = time.time()
        tmStartTime = time.time()
            
        while (tmCurrentTime - testTime < tmStartTime):
            # this could maybe be simplified in the future...
            dataDF = dataDF.append({'task' : '0_' + str(i) , 'time': time.time()},ignore_index=True)
            SolarServer.test_click("http://" + SERVER_IP + "/dropdown/dropdown_dynamic_limageA.html")
            tmCurrentTime = time.time()
            dataDF = dataDF.append({'task' : '0_' + str(i) , 'time': time.time()},ignore_index=True)
            SolarServer.test_click("http://" + SERVER_IP + "/dropdown/dropdown_dynamic_limageB.html")
            tmCurrentTime = time.time()

        SolarServer.tearDown()
        dataDF = dataDF.append({'task' : '0_' + str(i) + '_stop' , 'time': time.time()},ignore_index=True)

        #chill out between tests
        time.sleep(middleSleepTime)

        # Phase 2
        print ("Starting small test!")

        dataDF = dataDF.append({'task' : '1_' + str(i) + '_start', 'time': time.time()},ignore_index=True)
        SolarServer = SolarServerTest()

        tmCurrentTime = time.time()
        tmStartTime = time.time()
            
        while (tmCurrentTime - testTime < tmStartTime):
            dataDF = dataDF.append({'task' : '1_' + str(i) , 'time': time.time()},ignore_index=True)
            SolarServer.test_click("http://" + SERVER_IP + "/dropdown/dropdown_dynamic_simageA.html")
            tmCurrentTime = time.time()
            dataDF = dataDF.append({'task' : '1_' + str(i) , 'time': time.time()},ignore_index=True)
            SolarServer.test_click("http://" + SERVER_IP + "/dropdown/dropdown_dynamic_simageB.html")
            tmCurrentTime = time.time()

        SolarServer.tearDown()
        dataDF = dataDF.append({'task' : '1_' + str(i) + '_stop' , 'time': time.time()},ignore_index=True)

        #chill out between tests
        time.sleep(middleSleepTime)


    #save data to file
    try:
        with open(fileName) as csvfile:
            print("This file already exists!")
    except:
        dataDF.to_csv(fileName, sep=',',index=False)

    #60 seconds idle at the end
    time.sleep(bookendSleepTime)
    print("pingpong done")
    

if __name__ == "__main__":
    pingpongImage()
