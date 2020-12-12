<?php

$handle = fopen(__DIR__ . '/input.txt', 'r');
$numPasses = 0;

while ($line = fgets($handle)) {
    preg_match('/(\d+)\-(\d+) (\w)\: (\w+)/', $line, $matches);
    list ($full, $min, $max, $letter, $string) = $matches;

    $stringContains = substr_count($string, $letter);
    $pass = $stringContains <= $max && $stringContains >= $min;

    if ($pass) {
        $numPasses++;
    }
}

echo 'A:' . $numPasses . "\n";

rewind($handle);

$numPasses = 0;

while ($line = fgets($handle)) {
    preg_match('/(\d+)\-(\d+) (\w)\: (\w+)/', $line, $matches);
    list ($full, $first, $second, $letter, $string) = $matches;

    if ($string[$first - 1] === $letter ^ $string[$second - 1] === $letter) {
        $numPasses++;
    }
}

echo 'B:' . $numPasses . "\n";