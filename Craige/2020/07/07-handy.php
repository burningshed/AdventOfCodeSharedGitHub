<?php

require __DIR__.'/../vendor/autoload.php';

$file = file_get_contents(__DIR__.'/input.txt');
$i=0;
$tree = [];

foreach (explode("\n", $file) as $line) {
    $line = trim($line);
    preg_match('/^(.+?) bags contain (.+)/', $line, $matches);

    $bagColor = $matches[1];

    if (strpos($line, 'no other bags.') !== false) {
        $tree[$bagColor] = null;

        continue;
    }

    $contains = explode(',', $matches[2]);
    $bags = array_map(function ($bagLine) {
        return trim(substr($bagLine, 0, strlen(trim($bagLine, '.'))-4));
    }, $contains);

    $tree[$bagColor] = [];

    foreach ($bags as $bagLine) {
        preg_match('/^(\d+) (.+)$/', $bagLine, $matches);

        $tree[$bagColor][$matches[2]] = $matches[1];
    }
}

function doesRecurseToGold($tree, $color, $depth)
{
    if (isset($tree[$color]['shiny gold'])) {
        return true;
    }

    if ($tree[$color] === null) {
        return false;
    }

    foreach ($tree[$color] as $subColor => $num) {
        if (doesRecurseToGold($tree, $subColor, $depth+1)) {
            return true;
        }
    }

    return false;
}

function bagSum($tree, $color)
{
    $sum = 0;

    if ($tree[$color] === null) {
        return 0;
    }

    foreach ($tree[$color] as $subColor => $amount) {
        $sum += ($amount) + ($amount * bagSum($tree, $subColor));
    }

    return $sum;
}

$total = 0;
foreach ($tree as $color => $subs) {
    if (doesRecurseToGold($tree, $color, 0)) {
        $total++;
    }
}

dump([
    'partA' => $total,
    'tree' => $tree,
    'partB' => bagSum($tree, 'shiny gold'),
]);

