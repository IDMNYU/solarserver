# Charge Controller Data Tracer
This page is about the following two things.
- To read the data of the solar charge controller of Epver and saving it as csv or json.
- Do display a graph of the data from csv or json on html

(Originated from https://github.com/alexnathanson/EPSolar_Tracer)

## Read the data of the solar charge controller
### Hardwares
- Solar Charge Controller: We use [Eprver Tracer3210AN](https://www.epsolarpv.com/product/3.html), but any Eprver Tracer-AN Series would work.

- [Raspberry Pi 4 Model B 4GM RAM](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)

### Wiring
TBA (Please refer to https://github.com/alexnathanson/EPSolar_Tracer)

### Software Prerequisites
To install pymodbus

```
$ sudo pip3 install pymodbus
```
(If you don't have pip then run `$ sudo apt-get install python3-pip`)

To install Pandas

```
$ sudo apt install python3-pandas
```

## Run
### Test
To test to see if data is being read from the charge controller, run 

```
$ python3 test.py
```

### Data logging
To save charge controller data as csv, run

```
$ python3 csv_datalogger.py
```

To save charge controller data as json, run

```
$ python3 json_datalogger.py
```

By default, the data is saved every 60 seconds. If you want to change the interval, change the number of `sleep(60)`.

The data is stored under `data` folder. The data to be saved is as follows.

```
datetime: Python's datetime type
solarVoltage: V
solarCurrent: A
solarPowerL: W
solarPowerH: W
batteryVoltage: V
batteryCurrent: A
batteryPowerL: W
batteryPowerH: W
loadVoltage: V
loadCurrent: A
loadPower: W
batteryPercentage: In decimal
```

## Display data as a graph in HTML
This section explains how to set up a local server in Raspberry Pi and display the data as a graph using JavaScript and html.

### Host a website
Please refer to [Set up an Apache web server](https://projects.raspberrypi.org/en/projects/lamp-web-server-with-wordpress/2) and [Install PHP](https://projects.raspberrypi.org/en/projects/lamp-web-server-with-wordpress/3) to setup a server on Raspberry Pi.

### Display data
To display data, we use `index.php`, `data` folder, and `js` folder. Here we show two ways to do it, so you can choose the one you like: either place necessary files in the appropriate location or edit the apache server configuration to properly specify the path of the files.

#### Put files in the appropriate location
By default, the apache server will refer to `/var/www/html/`. So one way is put all the necessary files (`index.php`, `data` folder, and `js` folder) under `/var/www/html/`.

This method is easy, but has the disadvantage of being cumbersome to update files.

#### Edit the apache server configuration
Rather than moving the file to the proper location as described above, this method changes the Apache's settings and changes the path that the server refers to. For more information, please refer to [Changing apache2 document root in ubuntu 14.x](https://julienrenaux.fr/2015/04/06/changing-apache2-document-root-in-ubuntu-14-x/).

## Notes
All codes are still in progress.