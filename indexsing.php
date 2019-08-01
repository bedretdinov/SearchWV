<?php

include_once "./LibSearch.php";


$searchLib = new LibSearch();

$searchLib->Connection([
    'DB_HOST'=>'dev.db.teamber',
    'DB_PORT'=> 3307,
    'DB_USER'=>'develop',
    'DB_PASS'=>'ZW0rdypjKhfOxaA3eQ32',
    'DB_NAME'=>'biglion',
]);



$searchLib->MakeIndex('
    SELECT  df.DEAL_OFFER_ID as ID, df.TITLE as TEXT FROM DO_ACTIVE do
    inner JOIN DEAL_OFFER df ON df.DEAL_OFFER_ID = do.DO_ACTIVE_ID AND VERSION=1  
');