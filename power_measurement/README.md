This is a parent directory of the following two directories.
* [power_consumption](https://github.com/IDMNYU/solarserver/tree/master/power_measurement/power_consumption): To measure the energy consumption of a Raspberry Pi using another Raspberry Pi with INA219.
* [power_comparison](https://github.com/IDMNYU/solarserver/tree/master/power_measurement/power_comparison): To compare the energy consumptions of webserver on a Raspberry Pi hosting two different websites that shows different UI components by using Selenium, 

## Getting Started
### Hardwares
We use two Raspberry Pi and one INA219.
- One Raspberry Pi (Server-Pi) is used for a webserver to host a website.
- The other Raspberry Pi with INA219 (Measuring-Pi) is used for measuring the Server-Pi's power consumption.

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
Please refer to [Host a website](https://github.com/IDMNYU/solarserver/tree/master/charge_controller_data_tracer#host-a-website).

#### Other libraries
TBA

## Notes
All codes are still in progress.
