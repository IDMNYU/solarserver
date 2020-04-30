// read json and draw graph
function getjson() {
    var req = new XMLHttpRequest();
    req.overrideMimeType("application/json");
    req.open("get", "../data/tracerData2020-04-20.json", true); 
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var obj = JSON.parse(this.responseText);
            show(obj)
        }
    }
    req.send(null);
}

function show(json){
    var labels = json.map(function(e) {
        var date = new Date(e.datetime)
        var h = (date.getUTCHours()<10?'0':'') + date.getUTCHours();
        var m = (date.getUTCMinutes()<10?'0':'') + date.getUTCMinutes();
        return h + ':' + m;
    });

    var solar = json.map(function(e) {
        return e.solarVoltage;
    });

    var battery = json.map(function(e) {
        return e.batteryVoltage;
    });

    var ctx = document.getElementById("myBarChart");
    var config = {
        type: 'line',
        data: {
            labels: labels,
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
            }]
        },
        options: {
            title: {
                display: true,
                text: "Voltage"
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
    var chart = new Chart(ctx, config);
};

getjson();