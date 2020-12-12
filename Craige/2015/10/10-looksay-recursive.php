<?php

$string = '1113222113'; //113';

function recurse($string)
{
    $size = strlen($string);
    $mid = (int)($size / 2);
    $midChar = $string[$mid];
    $split = false;

    for ($i=$mid+1; $i<$size; $i++) {
        if ($midChar !== $string[$i]) {
            $split = true;
            break;
        }
    }

    // Went to end and didn't find another char
    if (!$split) {
        for ($i=$mid; $i >= 0; $i--) {
            if ($midChar !== $string[$i]) {
                $split = true;
                $i++;
                break;
            }
        }
    }

    // All chars match
    if (!$split) {
        return $size . $midChar;
    }

    $left = substr($string, 0, $i);
    $right = substr($string, $i);

    return recurse($left) . recurse($right);
}

$start = microtime(true);
for ($i=0; $i<50; $i++) {
    $output = recurse($string);
    $string = $output;
}
$end = microtime(true);

echo strlen($string) . ' in ' . ($end - $start) . ' seconds';