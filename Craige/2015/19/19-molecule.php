<?php

require __DIR__ .'/../vendor/autoload.php';

$input = array_map('trim', explode("\n", file_get_contents(__DIR__.'/input.txt')));
$rules = [];
$sequence = $input[count($input)-1];
$replacements = [];

foreach ($input as $line) {
    if (strpos($line, '=>') !== false) {
        list ($find, $replace) = explode(' => ', $line);

        if (!isset($rules[$find])) {
            $rules[$find] = [$replace];
        } else {
            $rules[$find][] = $replace;
        }
    }
}

for ($i=0; $i<strlen($sequence);) {
    for ($length = 1; $length <= 2; $length++) {
        $molecule = substr($sequence, $i, $length);

        if (isset($rules[$molecule])) {
            foreach ($rules[$molecule] as $replacement) {
                $full = substr($sequence, 0, $i) . $replacement . substr($sequence, $i);
                $replacements[$full] = true;
            }

            $i+=$length;
            break;
        }
    }

    $i++;
}

dump(count($replacements));