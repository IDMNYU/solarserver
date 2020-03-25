# Solar Server
Forked from https://github.com/alexnathanson/solarserver
This repo is now under heavy construction by Keita at IDM.

This project is 
- To host a webserver on Raspberry Pi powered by solor energy
- To measure the energy consumption of the server using another Raspberry Pi with INA219.
- To compare the energy consumptions of the server with different UI components using Selenium (i.e., difference of the energy consumptions of the server when hosting a large-data-size image and small-data-size image)

## Getting Started
### Hardwares
We use two Raspberry Pi and one INA219.
- One Raspberry Pi (Server-Pi) is for a webserver
- The other Raspberry Pi with INA219 (Measuring-Pi) is for measuring the Server-Pi's power consumption

## Running the codes
### Hosting a webserver on Server-Pi
Please refer to [Set up an Apache web server](https://projects.raspberrypi.org/en/projects/lamp-web-server-with-wordpress/2) and setup a server on Server-Pi.

### Measuring the energy consumption of Server-Pi
#### Prerequisites
See [Python Computer Wiring](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/python-circuitpython) for the wiring with Measuring-Pi and INA219.

Here is the wiring with Server-Pi and Measuring-Pi + INA219
(TBA)

First install `CircuitPython Library` on Measuring-Pi (See [Installing CircuitPython Libraries on Raspberry Pi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)).

Then install `adafruit-circuitpython-ina219` library via `sudo pip3 install adafruit-circuitpython-ina219` (See [Python Installation of INA219 Library](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/python-circuitpython#python-installation-of-ina219-library-7-6)) 

#### Run
Go to [energy_consumption](https://github.com/IDMNYU/solarserver/tree/master/energy_consumption)

```
$ cd energy_consumption/
```

Run

```
$ python3 json_ina219_datarecorder.py
```

Default interval is 60 seconds. Change `sleep(60)` as needed.

### Compare the energy consumptions with different UI components
#### Prerequisites
You need to install Selenium (firefox driver) on Measuring-Pi.

Install firefox on Measuring-Pi.

```$ sudo apt-get install firefox-esr```

Install seleinum
```$ sudo pip3 install selenium```

You also need a specific arm version (v0.23.0-arm7hf) of geckodriver to run selenium on RaspberryPi. 

```$ sudo wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-arm7hf.tar.gz```

Open it and move geckodriver to /usr/local/bin/

To test, run `Example 0` from https://pypi.org/project/selenium/.

You also need to put the `dropdown` folder under /var/www/html on your Server-Pi.

#### Run
Go to [energy_comparison](https://github.com/IDMNYU/solarserver/tree/master/energy_comparison)

```
$ cd energy_comparison/
```

Run the following code on Measuring-Pi with replacing IP-ADDRESS-OF-SERVER-PI to your Server-Pi's actual IP address

```python3 main.py IP-ADDRESS-OF-SERVER-PI```

`main.py` will run three programs:
- `ina219_datarecorder.py`: Measuring-Pi gets power consumption of Server-Pi and save `ina219-xxx.csv` file under `data` folder.
- `imagesize_pingpong.py`: Measuring-Pi accesses htmls in `dropdown` folder on Server-Pi which show large and small images and save `selenium-xxx.csv` file under `data` folder.
- `aggregator.py`: Compare `ina219-xxx.csv` and `selenium-xxx.csv`, and show some graphs.

## Notes
`aggregator.py` has some errors. All codes are still in progress.