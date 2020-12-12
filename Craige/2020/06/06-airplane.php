<?php

require __DIR__ . '/../vendor/autoload.php';

$groups = explode("\r\n\r\n", file_get_contents(__DIR__.'/input.txt'));
$total = 0;
$totalAll = 0;

foreach ($groups as $group) {
    $questions = preg_split('/\s+/', $group);
    $yeses = [];

    $splits = array_map('str_split', $questions);
    $joined = array_merge(...$splits);
    $unique = array_unique($joined);
    $correct = count($unique);

    $allAnswer = count($splits) > 1 ? array_intersect(...$splits) : $splits[0];
    $allCorrect = count($allAnswer);

    $total += $correct;
    $totalAll += $allCorrect;
}

dump([
    'partA' => $total,
    'partB' => $totalAll,
]);