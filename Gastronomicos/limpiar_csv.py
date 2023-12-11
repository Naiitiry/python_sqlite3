import pandas as pd

#Buscamos el archivo
ruta_archivo = 'C:/Users/Tangalanga/Desktop/Practicas de Python/python_sqlite3/Gastronomicos/oferta_gastronomica.csv'
df = pd.read_csv(ruta_archivo,sep=',')

#Declaramos las columnas a revisar
columnas_a_rellenar = ["long","lat","id","nombre","categoria","cocina","ambientacion","telefono","mail","horario","calle_nombre","calle_altura","calle_cruce","direccion_completa","barrio","comuna","codigo_postal","codigo_postal_argentino"]

# Rellenamos los espacios vacíos con 'No posee'
df[columnas_a_rellenar]=df[columnas_a_rellenar].fillna('No posee')

# Guardamos el resultado en el mismo CSV (se recomienda hacer una copia)
df.to_csv(ruta_archivo,sep=',',index=False)
print(df)