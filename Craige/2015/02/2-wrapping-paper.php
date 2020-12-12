<?php

include __DIR__ . '/../vendor/autoload.php';

$handle = fopen(__DIR__ . '/input.txt', 'r');
$total = 0;
$ribbon = 0;

while ($line = trim(fgets($handle))) {
    list ($l, $w, $h) = explode('x', $line);

    $values = [
        $l * $w,
        $l * $h,
        $w * $h,
    ];

    $sides = [(int)$l, (int)$w, (int)$h];
    asort($sides);

    $perimeter = $sides[0]*2 + $sides[1]*2;
    $volume = $l * $w * $h;

    $ribbon += $perimeter + $volume;

    $lowest  = min($values);
    $sum = array_sum($values) * (2) + $lowest;

    $total += $sum;
}

dump([
    'paper' => $total,
    'ribbon' => $ribbon
]);
