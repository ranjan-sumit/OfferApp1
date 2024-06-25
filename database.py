import psycopg2 as pg
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
import os
import nzpy

def net_conn():
    netezza_conn = nzpy.connect(user="CORP_SUPPORT",
                        password="Welcome@corp",
                        host='10.249.118.127',
                        port=5480, 
                        database="DM_CORP_SUPPORT",
                        securityLevel=1,
                        logLevel=0)
    return netezza_conn

def init_connection():
    
    postgre_uri = sqlalchemy.engine.URL.create("postgresql+psycopg2",
                                               username='promouser@psql-promotool-d.postgres.database.azure.com',
                                               database='c4apdb',
                                               host='10.101.1.4',
                                               password='^&*()%$#@!',
                                               port=5432)
    
    postgres_conn = create_engine(postgre_uri)
    return postgres_conn

postgres_conn = init_connection()




def get_offer_shareid(shareId):
    
    get_offer = pd.read_sql(f""" SELECT OFFER_4 FROM ADMIN.BUDDY_PROJECT WHERE card_key like '%{shareId}'; """, net_conn())
    return get_offer

def get_offer_emailid(email_id):
    
    get_offer = pd.read_sql(f""" SELECT * FROM ADMIN.BUDDY_PROJECT
WHERE CUST_EMAIL='{email_id}'
AND EMAIL_FLAG='VALID_FORMAT'; """, net_conn())
    return get_offer

def get_offer_phoneno(phoneno):
    
    get_offer = pd.read_sql(f""" SELECT * FROM ADMIN.BUDDY_PROJECT
WHERE CUST_MOBILE like '%{phoneno}' ; """, net_conn())
    return get_offer
