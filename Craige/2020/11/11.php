<?php

require __DIR__ . '/../vendor/autoload.php';

$lines = array_map('str_split', array_map('trim', explode("\n", file_get_contents(__DIR__.'/input.txt'))));

function debug($grid) {
    for ($y=0; $y<count($grid); $y++) {
        for ($x=0; $x<count($grid[$y]); $x++) {
            echo $grid[$y][$x];
        }

        echo "\n";
    }

    echo "\n";
}

function equal($grid1, $grid2) {
    foreach ($grid1 as $row => $value) {
        if ($grid1[$row] !== $grid2[$row]) {
            return false;
        }
    }

    return true;
}

function getNeighborCount($value, $grid, $xCheck, $yCheck)
{
    $total = 0;

    for ($y = max(0, $yCheck - 1); $y <= min(count($grid) - 1, $yCheck + 1); $y++) {
        for ($x = max(0, $xCheck - 1); $x <= min(count($grid[$yCheck]) - 1, $xCheck + 1); $x++) {
            // don't check yourself
            if ($x == $xCheck && $y === $yCheck) {
                continue;
            }

            if ($value === $grid[$y][$x]) {
                $total++;
            }
        }
    }

    return $total;
}

function getCardinalView($value, $grid, $xCheck, $yCheck)
{
    // Top going clockwise
    $directions = [
        [0, -1],  // n
        [1, -1],  // ne
        [1, 0],   // e
        [1, 1],   // se
        [0, 1],   // s
        [-1, 1],  // sw
        [-1, 0],  // w
        [-1, -1], // nw
    ];

    $total = 0;

    foreach ($directions as list($xInc, $yInc)) {
        $iterX = $xCheck;
        $iterY = $yCheck;

        while (true) {
            $iterX += $xInc;
            $iterY += $yInc;

            if ($iterX < 0 || $iterY < 0) {
                break;
            }

            if ($iterX > count($grid[0]) - 1 || $iterY > count($grid) - 1) {
                break;
            }

            $gridVal = $grid[$iterY][$iterX];

            if ($gridVal !== '.') {
                if ($gridVal === $value) {
                    $total++;
                }

                break;
            }
        }
    }

    return $total;
}

function run($grid)
{
    $copy = [];
    $copy = $grid;

    for ($y=0; $y<count($grid); $y++) {
        for ($x = 0; $x < count($grid[$y]); $x++) {
            $currentChar = $grid[$y][$x];

            // floor
            if ($currentChar === '.') {
                continue;
            }

            //$occupiedAdjacent = getNeighborCount('#', $copy, $x, $y);
            $occupiedVisible = getCardinalView('#', $copy, $x, $y);

            // empty
            if ($currentChar === 'L') {
                if ($occupiedVisible === 0) {
                    $grid[$y][$x] = '#';
                }
            }

            // occupado
            if ($currentChar === '#') {
                if ($occupiedVisible >= 5) {
                    $grid[$y][$x] = 'L';
                }
            }
        }
    }

    return $grid;
}

$start = microtime(true);
$grid = $lines;
for ($i=0; $i<1000; $i++) {
    $newGrid = run($grid);

    if (equal($grid, $newGrid)) {

        debug($newGrid);
        $total = 0;

        foreach ($newGrid as $row => $value) {
            $total += substr_count(implode('', $value), '#');
        }

        $end = microtime(true);

        dump([
            'total' => $total,
            'time' => round($end - $start, 3),
        ]);

        die();
    }

    $grid = $newGrid;
}



