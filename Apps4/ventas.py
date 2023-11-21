import pandas as pd
import numpy as np
#from scipy import stats
ventas=pd.read_csv("C:/Users/rdanchuk/Desktop/python/Python y SQLite/Formulario/Apps4/datos2/ventas.csv")
#print(ventas.columns)
#print(ventas['Importe'].count())
#print(ventas.dtypes)


# ******************** MEDIA ********************
# array_nros=np.array([12,5,6,8,2.8,8,52,63,8.3,698,156,12316.123,14,77,16])
# media=np.mean(array_nros)
# print(f'Promedio/media: {media:.2f}')

# ******************** MEDIANA ********************
# mediana=np.median(array_nros)
# print('Mediana',mediana)

# ******************** CUARTILES ********************
# q1=np.quantile(array_nros, .25)
# q2=np.quantile(array_nros, .50)
# q3=np.quantile(array_nros, .75)
# print(f'Q1={q1}, Q2={q2}, Q3={q3}')

# ******************** PERCENTIL ********************
# Mide en porcentaje
# p60=np.percentile(array_nros,60)
# p20=np.percentile(array_nros,20)
# print(f'Percentil 20={p20:.2f}, Percentil 60={p60:.2f}')

# ******************** MODA ********************
# no hay método en numpy, se debe importar un módulo
# from scipy import stats
# moda=stats.mode(array_nros)
# print('Moda',moda)

# ******************** VARIANZA ********************

# varianza=np.var(array_nros)
# print(f'{varianza:.2f}')

# ******************** DESVIO STANDARD ********************

# ds=np.std(array_nros)
# print(ds)
# print(ds**2) #esto es la varianza

# ******************** MATRIZ BI-DIMENSIONAL ********************

# l2=[[5,95,48],[15,4,653]]
# arr3=np.array(l2)
# print(arr3)
# para acceder a algún elemento del array, tengo que buscar su linea y columna, como si fuera los 
# índices de un array común, posición 0 para el primero, 1 para el segundo, etc
# print(arr3[1,2]) # => 653
# siendo que el 1 es el ROW y el 2 es el índice

