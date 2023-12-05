import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/Tangalanga/Desktop/Practicas de Python/python_sqlite3/Nombres/nombres_permitidos.csv', sep=';')
# print(df.dtypes)
'''
NOMBRE         object
SEXO           object
ORIGEN         object
SIGNIFICADO    object
dtype: object     
'''
df_count = len(df)
df_count_2 = df.shape[0]
# print(f'Conteo total con LEN: {df_count} y el conteo con SHAPE: {df_count_2}')

# BUSQUEDA DE NOMBRES POR PRIMERA LETRA
letra = 'A'
df_r = df[df['NOMBRE'].str.startswith(letra,na=False)]
# print(f'Nombres que empiezan con la letra {letra}:')

# CONTAR NOMBRES POR PRIMERA LETRA
# print(len(df_r))

# CONTAR NOMBRES CON SIGNIFICADO Y SIN SIGNIFICADO
re_signi = df['SIGNIFICADO'].value_counts()
# print(f'Recuento de S/S: {re_signi}')
recuento_ss = re_signi.get('S/S',0)
recuento_otros = re_signi.sum() - recuento_ss
# print(f'El recuento de S/S es de: {recuento_ss}\nY con significado son de: {recuento_otros}\n siendo un total de: {df_count}')

# ***********************************
# ********* MODIFICANDO CSV *********
# ***********************************

# mostramos csv sin modificar
# print(df)

nombre_a_modificar = input('Ingrese el nombre a modificar: ')

if nombre_a_modificar in df['NOMBRE'].values:
    # preguntamos por el origen y significado
    nuevo_origen = input("Ingrese nuevo origen: ")
    nuevos_significado = input("Ingrese nuevo significado: ")

    # modificar valores en el df
    df.loc[df['NOMBRE'] == nombre_a_modificar, 'ORIGEN'] = nuevo_origen
    df.loc[df['NOMBRE'] == nombre_a_modificar, 'SIGNIFICADO'] = nuevos_significado

    # Mostrar DF actualizado
    df.to_csv('C:/Users/Tangalanga/Desktop/Practicas de Python/python_sqlite3/Nombres/nombres_permitidos_actualizado.csv',index=False)

    print('Datos modificados correctamente.')
else:
    print(f'No se encontró registro con el nombre {nombre_a_modificar}.')