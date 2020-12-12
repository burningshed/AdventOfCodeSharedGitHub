<?php

require __DIR__ . '/../vendor/autoload.php';

$lines = array_map('trim', explode("\n", file_get_contents(__DIR__.'/input.txt')));
$maxId = 0;
$minId = 1000;
$seatSum = 0;

foreach ($lines as $line) {
    $rowString = str_replace(['F', 'B'], ['0', '1'], substr($line, 0, 7));
    $columnString = str_replace(['L', 'R'], ['0', '1'], substr($line, 7, 3));

    $row = bindec($rowString);
    $col = bindec($columnString);

    $id = $row * 8 + $col;
    $maxId = max($id, $maxId);
    $minId = min($id, $minId);

    $seatSum += $id;
}

$maxSum = $maxId * ($maxId + 1) / 2;
$minSum = $minId * ($minId - 1) / 2;
$sum = $maxSum - $minSum;
$seat = $sum - $seatSum;

dump([
    'partA' => $maxId,
    'minId' => $minId,
    'sum' => $seatSum,
    'seat' => $seat,
]);
