<?php

require __DIR__ . '/../vendor/autoload.php';

$lines = array_map('trim', explode("\n", file_get_contents(__DIR__.'/input-fixed.txt')));
$position = 0;
$accumulator = 0;
$visited = [];
$lastJmp = null;
$maxPos = 0;
$maxPot = 0;
$history = [];

function doesFinish($position, $visited, $accumulator, $alreadyChanged): bool
{
    global $lines;

    while (true) {
        if ($position >= count($lines)) {
            dump(['accumulator' => $accumulator]);

            return true;
        }

        if ($visited[$position] ?? false === true) {
            return false;
        } else {
            $visited[$position] = true;
        }

        $instructionString = $lines[$position];
        list($instruction, $valueString) = explode(' ', $instructionString);
        $value = intval($valueString);

        $history[] = 'Line '.$position.': '.$instructionString;

        if ($instruction === 'acc') {
            $accumulator += $value;
            $position++;
        } elseif ($instruction === 'jmp') {
            // Pretend it was a nop
            if (!$alreadyChanged && doesFinish($position + 1, $visited, $accumulator, true)) {
                dump('got a nop finish from line: ' . $position);
            }

            $lastJmp = [
                'position' => $position,
                'string' => $instructionString,
            ];

            $position += $value;
        } else {
            // Pretend it was a jmp and see if it finishes
            if (!$alreadyChanged && doesFinish($position + $value, $visited, $accumulator, true)) {
                dump('got a jmp finish from line: ' . $position);
            }

            $position++;
        }
    }
}

doesFinish(0, [], 0, false);
