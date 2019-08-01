
## Апи поиска
##### Поиск осуществляеться на основе нейросетей архитектуры WordToVec
   
Модель WordToVec обучен на основе текстов сайтов купанаторов   
Модуль использовался для поиска предложений более высокого уровня абстракции  
Для примера если поиск не находит слово ЕДА по вхлждению в офферы то он   
найдет его контексту [ кушать лакомиться питаться ]
   
###### описание обекта   
class LibSearch  
-- **Connection(array)** - Создает соеденение с базой  
-- **MakeIndex(sqlQuery)** - Индексирование данных ( структура запроса должна быть в 2 
колонки первый id элемента который будет возвращен 
во время поиска второе текст )   
-- **Search(array)**       - Поиск данных ( возвращает id элемента указанные в sql запросе методу MakeIndex )
  

```php  
<?php
# indexsing.php - Пример индексация данных

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
    SELECT  df.DEAL_OFFER_ID, df.TITLE as TITLE FROM DO_ACTIVE do
    inner JOIN DEAL_OFFER df ON df.DEAL_OFFER_ID = do.DO_ACTIVE_ID AND VERSION=1  
');
```
 

```php  
<?php 
# search.php - Пример создать запрос на поик

include_once "./LibSearch.php";

$searchLib = new LibSearch();
$queriesList = $searchLib->Search('ужин в ресторане'); # return dealoffer id

print_r($queriesList);
```

