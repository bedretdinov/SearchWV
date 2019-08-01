<?php

include_once "./LibSearch.php";

$searchLib = new LibSearch();
$queriesList = $searchLib->Search('замена стекла'); # return dealoffer id

print_r($queriesList);