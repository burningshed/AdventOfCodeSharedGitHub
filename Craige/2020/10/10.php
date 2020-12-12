<?php

require __DIR__ . '/../vendor/autoload.php';
/**

         0
         1
         4
      5  6  7

 *
 */


$lines = array_map('intval', array_map('trim', explode("\n", file_get_contents(__DIR__.'/input.txt'))));
$lines[] = 0;
$lines[] = max($lines) + 3;
// can take up to 3 jolts less on input
// adapter can do 3 higher than my highest
// seat is 0 (zero)

asort($lines);
$lines = array_values($lines);

$jumps = [
    1 => 0,
    2 => 0,
    3 => 0,
];

$combos = 0;
$lastLine = null;

foreach ($lines as $line) {
    if ($lastLine !== null) {
        $jumps[$line - $lastLine]++;
    }

    $lastLine = $line;
}

dump([
    'partA' => $jumps[1] * $jumps[3],
]);

function recurse($index)
{
    global $lines;

    if ($index >= count($lines)) {
        return 0;
    }

    $total = 0;
    $ways = [];

    for ($offset = 1; $offset <= 5; $offset++) {
        if ($index + $offset >= count($lines)) {
            break;
        }

        $current = $lines[$index];
        $next = $lines[$index + $offset];

        if ($next - $current <= 3) {
            $total++;
            $ways[] = [$current, $next];
        }
    }

    return $total;
}

$lookup = array_fill(0, count($lines), 0);
$lookup[0] = 1;

for ($i = 0; $i < count($lines) - 1; $i++) {
    for ($j = $i + 1; $j < count($lines) - 1; $j++) {
        if ($lines[$j] - $lines[$i] <= 3) {
            $lookup[$j] += $lookup[$i];
        } else {
            break;
        }
    }
}

dump($lookup);





