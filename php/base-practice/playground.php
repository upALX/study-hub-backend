<?php 

$varPHP = 'XXXX';

$counter = [];

$inc = 0;

$listCounter = [1,1,2,3,5,2,3,6,7];

foreach ($listCounter as $value) { 
    if (in_array( $value, array_keys($counter))) {
        $counter[$value]++;
    } else {
        $counter[$value] = 1;
    }
}

var_dump($counter);