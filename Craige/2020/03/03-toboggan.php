<?php

require __DIR__ . '/../vendor/autoload.php';

$lines = array_map('trim', explode("\n", file_get_contents(__DIR__.'/input.txt')));

$width = strlen($lines[0]);
$height = count($lines);

function check($x, $y, $lines)
{
    $modX = $x % strlen($lines[0]);

    if (!isset($lines[$y][$modX])) {
        return '.';
    }

    return $lines[$y][$modX];
}


function withSlope($xStep, $yStep)
{
    global $height, $lines; // gross

    $x = 0;
    $y = 0;
    $trees = 0;

    for ($h = 0; $h < $height; $h++) {
        $result = check($x, $y, $lines);

        if ($result === '#') {
            $trees++;
        }

        $x += $xStep;
        $y += $yStep;
    }

    return $trees;
}

$results = [
    withSlope(1, 1),
    withSlope(3, 1),
    withSlope(5, 1),
    withSlope(7, 1),
    withSlope(1, 2),
];

dump($results);
var_dump($results);
dump(array_product($results));
