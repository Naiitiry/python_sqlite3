import sqlite3 as sq3

# CONEXIÓN
def get_connetion():
    global name_database
    name_database = 'netflix_oscar.db'
    conn = sq3.connect(name_database)
    return conn

# DESCONEXIÓN
def close_connection():
    cursor.close()
    conn.close()

# CONSULTA
def read_database():
    is_conn = False
    try:
        global conn
        global cursor
        conn = get_connetion()
        cursor = conn.cursor()
        db_version = cursor.fetchone()
    except(Exception, sq3.Error) as error:
        print(f'Houston tenemos un problema: {error}')
    else:
        print(f'Estamos conectados en la BBDD {name_database}...')
        print(f'Con la version de SQLite: {db_version}')
        is_conn = True
    finally:
        if is_conn:
            close_connection()
            print('Se ha cerrado la conexión.')
