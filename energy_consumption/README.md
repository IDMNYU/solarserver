# Energy Consumption
This is to measure the energy consumption of Server-Pi using Measuring-Pi with INA219.

## Getting Started
### Hardware Prerequisites
See README at [solarserver](https://github.com/IDMNYU/solarserver).

### Software Prerequisites
See README at [solarserver](https://github.com/IDMNYU/solarserver).


## Run codes
```
$ cd energy_consumption/
$ python3 json_ina219_datarecorder.py
```

It will generate `JSON` file like the following.

```
[
	{
		"datetime": "2020-03-25T16:22:41.297335",
		"psu_voltage": 4.82905,
		"shunt_voltage": 0.04505000000000001,
		"bus_voltage": 4.784,
		"current": 0.4505,
		"power": 2.156
	} ,
	{
		"datetime": "2020-03-25T16:23:41.366596",
		"psu_voltage": 4.8251800000000005,
		"shunt_voltage": 0.045180000000000005,
		"bus_voltage": 4.78,
		"current": 0.45180000000000003,
		"power": 2.156
	}
]
```

Default save interval is 60 seconds. Change `sleep(60)` as needed.

Press `ctrl + C` to finish.