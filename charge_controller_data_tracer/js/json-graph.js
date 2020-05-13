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
            showData(obj);
        }
    }
    req.open("get", '/data/' + path, true);
    req.send(null);
}

function showData(json){
    var timeLabels = json.map(function(e) {
        var date = new Date(e.datetime);
        var h = (date.getUTCHours()<10?'0':'') + date.getUTCHours();
        var m = (date.getUTCMinutes()<10?'0':'') + date.getUTCMinutes();
        return h + ':' + m;
    });

    // voltage
    var solarVoltage = json.map(function(e) {return e.solarVoltage;});
    var batteryVoltage = json.map(function(e) {return e.batteryVoltage;});
    var loadVoltage = json.map(function(e) {return e.loadVoltage;});

    // current
    var solarCurrent = json.map(function(e) {return e.solarCurrent;});
    var batteryCurrent = json.map(function(e) {return e.batteryCurrent;});
    var loadCurrent = json.map(function(e) {return e.loadCurrent;});

    // power
    var solarPowerL = json.map(function(e) {return e.solarPowerL;});
    var batteryPowerL = json.map(function(e) {return e.batteryPowerL;});
    var loadPower = json.map(function(e) {return e.loadPower;});

    // power: not sure what to use but read them anyway
    var solarPowerH = json.map(function(e) {return e.solarPowerH;});
    var batteryPowerH = json.map(function(e) {return e.batteryPowerH;});

    var batteryPercentage = json.map(function(e) {return e.batteryPercentage*100;});

    // draw graphs and table
    showVoltage(timeLabels, solarVoltage, batteryVoltage, loadVoltage);
    showCurrent(timeLabels, solarCurrent, batteryCurrent, loadCurrent);
    showPower(timeLabels, solarPowerL, batteryPowerL, loadPower);
    showBatteryPercentage(timeLabels, batteryPercentage);
    showTable(timeLabels, solarVoltage, solarCurrent, solarPowerL, solarPowerH, batteryVoltage, batteryCurrent, batteryPowerL, batteryPowerH, loadVoltage, loadCurrent, loadPower, batteryPercentage);
    //showTable(json);
};

// global variables for each chart
var voltageChart=null;
var currentChart=null;
var powerChart=null;
var batteryPercentageChart=null;


function showVoltage(timeLabels, solarVoltage, batteryVoltage, loadVoltage) {
    var ctx = document.getElementById("voltageChart");
    var config = {
        type: 'line',
        data: {
            labels: timeLabels,
            datasets: [{
                label: 'Solar',
                data: solarVoltage,
                borderColor: 'rgba(154, 162, 235, 0.3)',
                fill: false
            }, {
                label: 'Battery',
                data: batteryVoltage,
                borderColor: 'rgba(54, 162, 235, 0.3)',
                fill: false
            }, {
                label: 'Load',
                data: loadVoltage,
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


function showCurrent(timeLabels, solarCurrent, batteryCurrent, loadCurrent) {
    var ctx = document.getElementById("currentChart");
    var config = {
        type: 'line',
        data: {
            labels: timeLabels,
            datasets: [{
                label: 'Solar',
                data: solarCurrent,
                borderColor: 'rgba(154, 162, 235, 0.3)',
                fill: false
            }, {
                label: 'Battery',
                data: batteryCurrent,
                borderColor: 'rgba(54, 162, 235, 0.3)',
                fill: false
            }, {
                label: 'Load',
                data: loadCurrent,
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


function showPower(timeLabels, solarPowerL, batteryPowerL, loadPower) {
    var ctx = document.getElementById("powerChart");
    var config = {
        type: 'line',
        data: {
            labels: timeLabels,
            datasets: [{
                label: 'Solar',
                data: solarPowerL,
                borderColor: 'rgba(154, 162, 235, 0.3)',
                fill: false
            }, {
                label: 'Battery',
                data: batteryPowerL,
                borderColor: 'rgba(54, 162, 235, 0.3)',
                fill: false
            }, {
                label: 'Load',
                data: loadPower,
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


function showBatteryPercentage(timeLabels, batteryPercentage) {
    var ctx = document.getElementById("batteryPercentage");
    var config = {
        type: 'line',
        data: {
            labels: timeLabels,
            datasets: [{
                label: 'Battery',
                data: batteryPercentage,
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

//function showTable(timeLabels, solarVoltage, showCurrent, solarPowerL, solarPowerH, batteryVoltage, batteryCurrent, batteryPowerL, batteryPowerH, loadVoltage, loadCurrent, loadPower, batteryPercentage) {
/*
function showTable(json) {
    txt = ""
    txt += showHeader(json, txt);
    //showContent(txt);
    document.getElementById("dataTable").innerHTML = txt;
}
*/

function showTable(timeLabels, solarVoltage, solarCurrent, solarPowerL, solarPowerH, batteryVoltage, batteryCurrent, batteryPowerL, batteryPowerH, loadVoltage, loadCurrent, loadPower, batteryPercentage) {
    var txt = "";

    txt += "<tr>"
    txt += "<th>" + "Time" + "</td>";
    txt += "<th>" + "Solar Voltage" + "</td>";
    txt += "<th>" + "Solar Current" + "</td>";
    txt += "<th>" + "Solar Power L" + "</td>";
    txt += "<th>" + "Solar Power H" + "</td>";
    txt += "<th>" + "Battery Voltage" + "</td>";
    txt += "<th>" + "Battery Current" + "</td>";
    txt += "<th>" + "Battery Power L" + "</td>";
    txt += "<th>" + "Battery Power H" + "</td>";
    txt += "<th>" + "Load Voltage" + "</td>";
    txt += "<th>" + "Load Current" + "</td>";
    txt += "<th>" + "Load Power" + "</td>";
    txt += "<th>" + "Battery Percentage" + "</td>";
    txt += "</th>"

    for (var i = 0; i < timeLabels.length; i++) {
        txt += "<tr>";
        txt += "<td>" + timeLabels[i] + "</td>";
        txt += "<td>" + solarVoltage[i] + "</td>";
        txt += "<td>" + solarCurrent[i] + "</td>";
        txt += "<td>" + solarPowerL[i] + "</td>";
        txt += "<td>" + solarPowerH[i] + "</td>";
        txt += "<td>" + batteryVoltage[i] + "</td>";
        txt += "<td>" + batteryCurrent[i] + "</td>";
        txt += "<td>" + batteryPowerL[i] + "</td>";
        txt += "<td>" + batteryPowerH[i] + "</td>";
        txt += "<td>" + loadVoltage[i] + "</td>";
        txt += "<td>" + loadCurrent[i] + "</td>";
        txt += "<td>" + loadPower[i] + "</td>";
        txt += "<td>" + parseInt(batteryPercentage[i]) + "</td>";
        txt += "</tr>";
    }
    document.getElementById("dataTable").innerHTML = txt;
}
