<!DOCTYPE html>
<html>

<head>
<h1>Solar Server!</h1>
</head>

<body>

<?php

//variables
$fileName = "/home/pi/EPSolar_Tracer/data/tracerData" . date("Y-m-d") . ".csv";
$rawDataArray = [];

echo "<h3>Today's date:</h3>" . date("Y-m-d") . "<br>";

echo "<h3>File name:</h3>". $fileName . "<br>";

// current directory
//echo getcwd() . "\n";

echo "<h3>PV Data:</h3>";

// Open the file for reading (from https://phpenthusiast.com/blog/parse-csv-with-php)
if (($h = fopen("{$fileName}", "r")) !== FALSE) 
{
  // Each line in the file is converted into an individual array that we call $data
  // The items of the array are comma separated
  while (($data = fgetcsv($h, 1000, ",")) !== FALSE) 
  {
    // Each individual array is being pushed into the nested array
    $rawDataArray[] = $data;		
  }

  // Close the file
  fclose($h);
}

// Display the code in a readable format
echo "<pre>";
var_dump($rawDataArray);
echo "</pre>";

//also from https://phpenthusiast.com/blog/parse-csv-with-php
$build = '<table><thead><th>item 1</th><th>item 2</th><th>item 3</th></thead><tbody>';
foreach($rawDataArray as $row)
{
$build .= '<tr>';
foreach($row as $item)
{
$build .= "<td>{$item}</td>";
}
$build .= '</tr>';
}
$build .= '</tbody></table>';
echo $build;
?>

</body>
</html>