<?php

require __DIR__ . '/../vendor/autoload.php';

$lines = array_map('intval', array_map('trim', explode("\n", file_get_contents(__DIR__.'/input.txt'))));
$history = [];
$lineNum = 0;

function getPairs($total)
{
    global $history;

    $pairs = [];

    foreach ($history as $num1) {
        foreach ($history as $num2) {
            if ($num1 === $num2) {
                continue;
            }

            if ($num1 + $num2 === $total) {
                $pairs[] = [$num1, $num2];
            }
        }
    }

    return count($pairs) > 0;
}

$partBSum = null;
foreach ($lines as $line) {
    $value = intval($line);

    if ($lineNum++ > 25 && !getPairs($value)) {
        $partBSum = $value;
    }

    $history[] = $line;

    if (count($history) > 25) {
        array_shift($history);
    }
}

for ($start = 0; $start < count($lines); $start++) {
    $length = 2;

    while (true) {
        $sum = array_sum($s = array_slice($lines, $start, $length));
        $length++;

        if ($sum == $partBSum) {
            $partB = min($s) + max($s);
            dump([
                'partA' => $partBSum,
                'partB' => $partB
            ]);
            die();
        }

        if ($sum > $partBSum) {
            break;
        }
    }
}
