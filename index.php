<!DOCTYPE html>
<html>

<head>
Solar Server!
</head>

<body>

<?php

//variables
$pvVoltsNow = 3;
$pvCurrentNow = .33;
$pvPowerNow = 1;

$dataNow = array($pvVoltsNow, $pvCurrentNow, $pvPowerNow);

echo json_encode($dataNow);

?>

</body>
</html>