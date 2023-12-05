from practicadeepnote import get_conn,close_conn
import sqlite3 as sq3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Mostrar los no nulos de la BBDD.

def no_nulos(col_name):
    get_conn()
    query = f'SELECT count(*) FROM content WHERE {col_name} IS NOT NULL'
    cur.execute(query)
    resultado=cur.fetchall()
    df=pd.DataFrame(resultado)
    print(df)
    close_conn()
no_nulos('title_content')