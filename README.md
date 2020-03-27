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
- One Raspberry Pi (Server-Pi) is for a webserver.
- The other Raspberry Pi with INA219 (Measuring-Pi) is for measuring the Server-Pi's power consumption.

### Wiring
#### Wiring with Measuring-Pi and INA219.
See [Python Computer Wiring](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/python-circuitpython).

#### Wiring with Server-Pi and Measuring-Pi + INA219
![Wiring with Server-Pi and Measuring-Pi + INA219](https://github.com/IDMNYU/solarserver/blob/master/images/wiring.png)

### Software Prerequisites
#### To use INA219
First, install `CircuitPython Library` on Measuring-Pi. See [Installing CircuitPython Libraries on Raspberry Pi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi) and follow the steps from "Update Your Pi and Python" till "Blinka Test".

Then, install `adafruit-circuitpython-ina219` library via `$ sudo pip3 install adafruit-circuitpython-ina219` (See [Python Installation of INA219 Library](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/python-circuitpython#python-installation-of-ina219-library-7-6) for the detail).

#### Other libraries
TBA


## What you can do
### Hosting a webserver on Server-Pi
Please refer to [Set up an Apache web server](https://projects.raspberrypi.org/en/projects/lamp-web-server-with-wordpress/2) and setup a server on Server-Pi.

### Measuring the energy consumption of Server-Pi
This is to measure the energy consumption of Server-Pi using Measuring-Pi with INA219. See [energy_consumption](https://github.com/IDMNYU/solarserver/tree/master/energy_consumption) for more detail.

### Compare the energy consumptions with different UI components
This is to compare the energy consumptions of the server with different UI components using Selenium. See [energy_comparison](https://github.com/IDMNYU/solarserver/tree/master/energy_comparison) for more detail.


## Notes
All codes are still in progress.