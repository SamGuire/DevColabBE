from psycopg2.pool import SimpleConnectionPool
import psycopg2
from app import config
import sys
import weakref

MIN_CONNECTION_POOL = 1
MAX_CONNECTION_POOL = 20

class DBConnnection:
    _instance = None
    _pool = None
    def __new__(cls,*args,**kwargs):
        if not DBConnnection._instance :
            DBConnnection._instance = object.__new__(cls)
        return DBConnnection._instance

    def __init__(self,config:'config.AppConfig') :
        self.db = {
            'host':config.POSTGRES_HOST,
            'database':config.POSTGRES_DATABASE,
            'port':config.POSTGRES_PORT,
            'user':config.POSTGRES_USERNAME,
            'password':config.POSTGRES_PASSWORD
        }
        if not DBConnnection._pool :
            try :
                DBConnnection._pool = SimpleConnectionPool(MIN_CONNECTION_POOL,MAX_CONNECTION_POOL,**self.db)
                print('Successfully created pooling for DB !')
            except (Exception,psycopg2.DatabaseError) as error :
                print('Error trying to connect to the database !',error)
    
    ## Work around regarding cleaning up the singleton object, to be called on app system exit
    def cleanup() :
        try :
            DBConnnection._pool.closeall()
            print('Closed all connections !')
        except Exception as e :
            print('Error trying to close all connections !',e)






