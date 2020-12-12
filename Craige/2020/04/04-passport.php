<?php

require __DIR__ . '/../vendor/autoload.php';

class Passport
{
    private array $properties;

    public function __construct(array $properties)
    {
        $this->properties = $properties;
    }

    public function has($property): bool
    {
        return array_key_exists($property, $this->properties);
    }

    public function get($property): string
    {
        return $this->properties[$property];
    }

    public function all(): array
    {
        return $this->properties;
    }
}

interface Validator
{
    public function valid(Passport $passport): bool;
}

class SimplePassportValidator implements Validator
{
    const REQUIRED_FIELDS = [
        'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',
    ];

    public function valid(Passport $passport): bool
    {
        foreach (self::REQUIRED_FIELDS as $field) {
            if (!$passport->has($field)) {
                return false;
            }
        }

        return true;
    }
}

class ValuePassportValidator implements Validator
{
    public function valid(Passport $passport): bool
    {
        $validators = self::getValueValidations();

        foreach ($passport->all() as $key => $value) {
            if (!isset($validators[$key])) {
                continue;
            }

            if (!$validators[$key]($value)) {
                return false;
            }
        }

        return true;
    }

    public static function getValueValidations(): array
    {
        return [
            'byr' => function ($year) {
                return strlen($year) === 4 && $year >= 1920 && $year <= 2004;
            },

            'iyr' => function ($year) {
                return strlen($year) === 4 && $year >= 2010 && $year <= 2020;
            },

            'eyr' => function ($year) {
                return strlen($year) === 4 && $year >=2020 && $year <= 2030;
            },

            'hgt' => function ($height) {
                $match = preg_match('/(\d+)(cm|in)/', $height, $matches);

                if ($match === 0) {
                    return false;
                }

                list ($fullMatch, $value, $units) = $matches;

                if ($units === 'cm') {
                    return $value >= 150 && $value <= 193;
                }

                if ($units === 'in') {
                    return $value >= 59 && $value <= 76;
                }

                return false;
            },

            'hcl' => function ($color) {
                return preg_match('/\#[0-9a-f]{6}/', $color) === 1;
            },

            'ecl' => function ($color) {
                return in_array(trim($color), ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']);
            },

            'pid' => function ($id) {
                dump($id);
                return preg_match('/^\d{9}$/', $id) === 1;
            }
        ];
    }
}

class ChainValidator implements Validator
{
    /**
     * @var Validator[]
     */
    private array $validators;

    public function __construct(array $validators)
    {
        $this->validators = $validators;
    }

    public function valid(Passport $passport): bool
    {
        foreach ($this->validators as $validator) {
            if (!$validator->valid($passport)) {
                return false;
            }
        }

        return true;
    }
}

class PassportParser
{
    public function parse($passportText): Passport
    {
        $matches = preg_split('/\s+/', $passportText);
        $pairs = [];

        foreach ($matches as $match) {
            list ($key, $value) = explode(':', $match);
            $pairs[$key] = $value;
        }

        return new Passport($pairs);
    }
}

$passports = explode("\r\n\r\n", file_get_contents(__DIR__.'/input.txt'));
$parser = new PassportParser();
$simpleValidator = new SimplePassportValidator();
$valueValidator = new ValuePassportValidator();
$chainValidator = new ChainValidator([$simpleValidator, $valueValidator]);
$partA = 0;
$partB = 0;

foreach ($passports as $passportText) {
    $passport = $parser->parse($passportText);

    if ($simpleValidator->valid($passport)) {
        $partA++;
    }

    if ($chainValidator->valid($passport)) {
        $partB++;
    }
}

dump([
    'partA' => $partA,
    'partB' => $partB,
]);