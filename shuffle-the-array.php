<?php
function _shuffle($nums, $n) {
    $nums2 = [];
    $arrResult = [];
    for ($o = $n; $o < count($nums); $o++) {
        array_push($nums2, $nums[$o]);
    }
    for ($i = 0; $i < count($nums); $i++) {
        if (count($arrResult) == 0) {
            $x = 0;
        } else {
            $x += 1;
        }
        if (count($arrResult) == $n * 2) {
            break;
        } else {
            array_push($arrResult, $nums[$i]);
            $checkInv = count($arrResult);
            for ($j = 0; $j < count($nums2); $j++) {
                if (count($arrResult) > $checkInv) {
                    break;
                } else {
                    array_push($arrResult, $nums2[$j + $x]);
                };
            };
        };
    };
    return $arrResult;
}

$numsx = [1, 2, 3, 4,5,6];
$nx = 3;

print_r(_shuffle($numsx, $nx));

//18ms

?>