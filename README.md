# Solar Server
Forked from https://github.com/alexnathanson/solarserver

This project is 
- [charge_controller_data_tracer](https://github.com/IDMNYU/solarserver/tree/master/charge_controller_data_tracer): To host a web server on Raspberry Pi to show a website that displays the data from the solar charge controller.
- [energy_consumption](https://github.com/IDMNYU/solarserver/tree/master/energy_consumption): To measure the energy consumption of a Raspberry Pi using another Raspberry Pi with INA219.
- [energy_comparison](https://github.com/IDMNYU/solarserver/tree/master/energy_comparison): To compare the energy consumptions of webserver on a Raspberry Pi hosting two different websites that shows different UI components by using Selenium, 

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
#### Use INA219
First, install `CircuitPython Library` on Measuring-Pi. See [Installing CircuitPython Libraries on Raspberry Pi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi) and follow the steps from "Update Your Pi and Python" till "Blinka Test".

Then, install `adafruit-circuitpython-ina219` library via `$ sudo pip3 install adafruit-circuitpython-ina219` (See [Python Installation of INA219 Library](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/python-circuitpython#python-installation-of-ina219-library-7-6) for the detail).

#### Host a website
Please refer to [Set up an Apache web server](https://projects.raspberrypi.org/en/projects/lamp-web-server-with-wordpress/2) and [Install PHP](https://projects.raspberrypi.org/en/projects/lamp-web-server-with-wordpress/3) to setup a server on Raspberry Pi.

#### Other libraries
TBA

## Notes
All codes are still in progress.
