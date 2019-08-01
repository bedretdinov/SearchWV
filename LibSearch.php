<?php



class LibSearch
{
    const PREF='.py';

    private $PYTIHN_PATH = "./venv/bin/python3";
    private $MODULE_PATH = "./lib.search/";

    private $connectionData = [];
    private $connectionConf = './lib.search/conf.json';

    public function Connection(array $option)
    {
        $this->connectionData = [
                'DB_HOST'=> $option['DB_HOST'],
                'DB_PORT'=> $option['DB_PORT'],
                'DB_USER'=> $option['DB_USER'],
                'DB_PASS'=> $option['DB_PASS'],
                'DB_NAME'=> $option['DB_NAME'],
                'MD_SUM'=> md5(serialize($option)),
        ];

        if(file_exists($this->connectionConf))
        {
            $confData   = file_get_contents($this->connectionConf);
            $conf       = json_decode($confData);

            if($conf->MD_SUM==$this->connectionData['MD_SUM'])
            {
                return False;
            }

        }

        file_put_contents($this->connectionConf, json_encode($this->connectionData));

    }

    public function MakeIndex($sqlQuery = '')
    {
        if(gettype($sqlQuery)!='string')
        {
            new Exception('Invalid argument type, must be string');
        }

        $res = $this->ExecModule('makemodel',$str_param = $sqlQuery);
        print_r($res);
    }

    public function Search($query=''):array
    {
        if($query==''){
            return [];
        }

        $resultList = $this->ExecModule('search',$query);
        print($resultList);
        return $resultList;
    }

    private function ExecModule($modeuleName, $strParam = '')
    {
        if($modeuleName=='' or $modeuleName==null)
        {
            new Exception('modeuleName is requirement parametr');
        }

        if(gettype($strParam)!='string')
        {
            new Exception('Invalid argument type, must be string');
        }

        $output = shell_exec(implode(' ',[
            $this->PYTIHN_PATH,
            $this->MODULE_PATH.$modeuleName.self::PREF,
            '"'.$strParam.'"'
        ]));

        return  json_decode($output);
    }
}