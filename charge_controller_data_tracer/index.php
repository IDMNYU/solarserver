<!DOCTYPE html>
<html>
<head>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.1.4/Chart.min.js"></script>
	<script type="text/javascript" src="js/json-graph.js"></script>
	<title>Charge Controller Graph</title>
</head>
<body>


<?php 
// get json files in directory
// https://www.php.net/manual/en/function.scandir.php
$directory = getcwd() . '/data';
$files = array_diff(scandir($directory), array('..', '.'));

// pass json file to javascript to show graph
foreach($files as $file){
    // https://stackoverflow.com/questions/9702040/how-pass-reference-to-this-on-href-javascript-function
    echo "<a id='$file' href='#$file' onClick=getjson('$file'); return false;>$file</a><br>";
}

?>

<canvas id="voltageChart"></canvas>
<canvas id="currentChart"></canvas>
<canvas id="powerChart"></canvas>
<canvas id="batteryPercentage"></canvas>

</body>
</html>
