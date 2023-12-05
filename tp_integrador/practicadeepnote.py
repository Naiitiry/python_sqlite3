import sqlite3 as sq3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# CONEXIÓN
def get_conn():
    global conn
    global cur
    conn=sq3.connect('../PYTHON_SQLITE3/tp_integrador/netflix_oscar.db')
    cur=conn.cursor()
    print('Se ha conectado a la BBDD.')
    return conn,cur

# DESCONEXIÓN
def close_conn():
    conn.close()

get_conn()
query='select * from content'
dft=pd.read_sql_query(query,conn)
df_no_nulos=dft.notnull().sum()
tabla=df_no_nulos.to_frame().T
print(tabla)