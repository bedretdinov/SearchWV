import pandas as pd
import pymysql.cursors
import json
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

class DataBase():
    connect = None

    @staticmethod
    def Slave(sql):

        with open('conf.json','rb') as f:
            confContent = f.read()
            conf = json.loads(confContent)

        DataBase.connect = pymysql.connect(host=conf['DB_HOST'],
                                           user=conf['DB_USER'],
                                           port=conf['DB_PORT'],
                                           password=conf['DB_PASS'],
                                           db=conf['DB_NAME'],
                                           charset='utf8',
                                           cursorclass=pymysql.cursors.DictCursor)
        return DataBase.query(sql)

    @staticmethod
    def query(sql):
        cursor = DataBase.connect.cursor()
        cursor.execute(sql)
        return pd.DataFrame(list(cursor.fetchall()))

