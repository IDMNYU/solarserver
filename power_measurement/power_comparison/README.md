# Energy Comparison
This is to compare the power consumptions of the server with different UI components using Selenium. For now, it only supports comparing the power consumptions of the server when hosting a large-data-size image and small-data-size image.

## Getting Started
### Install Selenium (firefox driver) on Measuring-Pi.
You need to install Selenium (firefox driver) on Measuring-Pi.

Install firefox on Measuring-Pi.

```
$ sudo apt-get install firefox-esr
```

Install seleinum.

```
$ sudo pip3 install selenium
```

You also need a specific arm version of geckodriver (v0.23.0-arm7hf) to run selenium on RaspberryPi.

```
$ sudo wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-arm7hf.tar.gz
```

Open it and move geckodriver to /usr/local/bin/

To test, run `Example 0` from https://pypi.org/project/selenium/.

### Place html files in Server-Pi
Please do either of the following.
- Move the `dropdown` folder under `/var/www/html` which the apache server will refer to by default.
- Change the apache server configuration. See [Display data](https://github.com/IDMNYU/solarserver/tree/master/charge_controller_data_tracer#display-data) for more detail.

## Run codes
```
$ cd energy_comparison/
$ python3 main.py IP-ADDRESS-OF-SERVER-PI
```

, where `IP-ADDRESS-OF-SERVER-PI` is your Server-Pi's actual IP address.


`main.py` runs three programs and does the following:
- `ina219_datarecorder.py`: Measuring-Pi gets power consumption of Server-Pi and save `ina219-xxx.csv` file under `data` folder.
- `imagesize_pingpong.py`: Measuring-Pi accesses html files in `dropdown` folder on Server-Pi which show large and small images. This is done in background so the actual web browser does not open. The test is repeated three times and save data as `selenium-xxx.csv` file under `data` folder. To change the times of the test, modify `times = 3` in line 70.
- `aggregator.py`: Compare `ina219-xxx.csv` and `selenium-xxx.csv`, and save three graphs, `volts.png`, `watts.png`, and `currents.png`.

## Notes
`aggregator.py` has some errors. All codes are still in progress.