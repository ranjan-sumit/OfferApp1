# import psycopg2 as pg
# import sqlalchemy
# from sqlalchemy import create_engine
# import pandas as pd
# import os
# import nzpy

# def net_conn():
    
#     return netezza_conn

# def init_connection():
    

    
#     postgres_conn = create_engine(postgre_uri)
#     return postgres_conn

# postgres_conn = init_connection()




# def get_offer_shareid(shareId):
    
#     get_offer = pd.read_sql(f""" SELECT OFFER_4 FROM ADMIN.BUDDY_PROJECT WHERE card_key like '%{shareId}'; """, net_conn())
#     return get_offer

# def get_offer_emailid(email_id):
    
#     get_offer = pd.read_sql(f""" SELECT * FROM ADMIN.BUDDY_PROJECT
# WHERE CUST_EMAIL='{email_id}'
# AND EMAIL_FLAG='VALID_FORMAT'; """, net_conn())
#     return get_offer

# def get_offer_phoneno(phoneno):
    
#     get_offer = pd.read_sql(f""" SELECT * FROM ADMIN.BUDDY_PROJECT
# WHERE CUST_MOBILE like '%{phoneno}' ; """, net_conn())
#     return get_offer
