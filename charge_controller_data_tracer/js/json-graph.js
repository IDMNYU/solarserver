// read json and draw graph
function getjson(path) {
    // https://reffect.co.jp/html/xmlhttprequest-basic
    let req = new XMLHttpRequest();
    req.overrideMimeType("application/json");
    //req.responseType = 'json';
    req.onreadystatechange = function() {
        if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
            let obj = JSON.parse(this.responseText);
            //let obj = this.response;
            show(obj);
        }
    }
    req.open("get", '/data/' + path, true);
    req.send(null);
}

function show(json){
    var timeLabels = json.map(function(e) {
        var date = new Date(e.datetime)
        var h = (date.getUTCHours()<10?'0':'') + date.getUTCHours();
        var m = (date.getUTCMinutes()<10?'0':'') + date.getUTCMinutes();
        return h + ':' + m;
    });

    showVoltage(timeLabels, json);
    showCurrent(timeLabels, json);
    showPower(timeLabels, json);

};


var voltageChart=null;

function showVoltage(timeLabels, json) {
    var solar = json.map(function(e) {
        return e.solarVoltage;
    });

    var battery = json.map(function(e) {
        return e.batteryVoltage;
    });

    var load = json.map(function(e) {
        return e.loadVoltage;
    });

    var ctx = document.getElementById("voltageChart");
    var config = {
        type: 'line',
        data: {
            labels: timeLabels,
            datasets: [{
                label: 'Solar',
                data: solar,
                borderColor: 'rgba(154, 162, 235, 0.3)',
                fill: false
            }, {
                label: 'Battery',
                data: battery,
                borderColor: 'rgba(54, 162, 235, 0.3)',
                fill: false
            }, {
                label: 'Load',
                data: load,
                borderColor: 'rgba(192,192,192,0.3)',
                fill: false
            }]
        },
        options: {
            title: {
                display: true,
                text: "Voltage (V)"
            },
            responsive: true,
            scales: {
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: "time (hh/mm)"
                    }
                }],
                yAxes: [{
                    type: "linear",
                    position: "left",
                    ticks: {
                        max: 20,
                        min: 10,
                        stepSize: 0.5
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "voltage (V)"
                    }
                }]
            }
        }
    }

    if (window.voltageChart) {
        window.voltageChart.destroy();
    }
    window.voltageChart = new Chart(ctx, config);
}


var currentChart=null;

function showCurrent(timeLabels, json) {
    var solar = json.map(function(e) {
        return e.solarCurrent;
    });

    var battery = json.map(function(e) {
        return e.batteryCurrent;
    });

    var load = json.map(function(e) {
        return e.loadCurrent;
    });

    var ctx = document.getElementById("currentChart");
    var config = {
        type: 'line',
        data: {
            labels: timeLabels,
            datasets: [{
                label: 'Solar',
                data: solar,
                borderColor: 'rgba(154, 162, 235, 0.3)',
                fill: false
            }, {
                label: 'Battery',
                data: battery,
                borderColor: 'rgba(54, 162, 235, 0.3)',
                fill: false
            }, {
                label: 'Load',
                data: load,
                borderColor: 'rgba(192,192,192,0.3)',
                fill: false
            }]
        },
        options: {
            title: {
                display: true,
                text: "Current (A)"
            },
            responsive: true,
            scales: {
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: "time (hh/mm)"
                    }
                }],
                yAxes: [{
                    type: "linear",
                    position: "left",
                    ticks: {
                        max: 0.5,
                        min: 0,
                        stepSize: 0.1
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "current (A)"
                    }
                }]
            }
        }
    }

    if (window.currentChart) {
        window.currentChart.destroy();
    }
    window.currentChart = new Chart(ctx, config);
}


var powerChart=null;

function showPower(timeLabels, json) {
    var solar = json.map(function(e) {
        return e.solarPowerL;
    });

    var battery = json.map(function(e) {
        return e.batteryPowerL;
    });

    var load = json.map(function(e) {
        return e.loadPower;
    });

    var ctx = document.getElementById("powerChart");
    var config = {
        type: 'line',
        data: {
            labels: timeLabels,
            datasets: [{
                label: 'Solar',
                data: solar,
                borderColor: 'rgba(154, 162, 235, 0.3)',
                fill: false
            }, {
                label: 'Battery',
                data: battery,
                borderColor: 'rgba(54, 162, 235, 0.3)',
                fill: false
            }, {
                label: 'Load',
                data: load,
                borderColor: 'rgba(192,192,192,0.3)',
                fill: false
            }]
        },
        options: {
            title: {
                display: true,
                text: "Power (W)"
            },
            responsive: true,
            scales: {
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: "time (hh/mm)"
                    }
                }],
                yAxes: [{
                    type: "linear",
                    position: "left",
                    ticks: {
                        max: 10,
                        min: 0,
                        stepSize: 1
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "power (W)"
                    }
                }]
            }
        }
    }

    if (window.powerChart) {
        window.powerChart.destroy();
    }
    window.powerChart = new Chart(ctx, config);
}


var batteryPercentageChart=null;

function showPower(timeLabels, json) {

    var battery = json.map(function(e) {
        return e.batteryPercentage*100;
    });

    var ctx = document.getElementById("batteryPercentage");
    var config = {
        type: 'line',
        data: {
            labels: timeLabels,
            datasets: [{
                label: 'Battery',
                data: battery,
                borderColor: 'rgba(54, 162, 235, 0.3)',
                fill: false
            }]
        },
        options: {
            title: {
                display: true,
                text: "Battery Percentage (%)"
            },
            responsive: true,
            scales: {
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: "time (hh/mm)"
                    }
                }],
                yAxes: [{
                    type: "linear",
                    position: "left",
                    ticks: {
                        max: 100,
                        min: 0,
                        stepSize: 10
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "percentage (%)"
                    }
                }]
            }
        }
    }

    if (window.batteryPercentageChart) {
        window.batteryPercentageChart.destroy();
    }
    window.batteryPercentageChart = new Chart(ctx, config);
}


//getjson();