#se importa el bd y se crea un data frame
import pandas as pd 
import sqlite3

df = pd.read_csv('vgsales.csv')
print (df.head())

#eliminar duplicados
df = df.drop_duplicates()

#Rellenar valores nulos
df = df.fillna("Unknown")

#Convertir año a entero (algunos vienen como float o NaN)
df['Year'] = pd.to_numeric(df['Year'], errors='coerce').fillna(0).astype(int)

# Crear una métrica: ventas totales por genero
sales_by_genre = df.groupby("Genre") ["Global_Sales"].sum().reset_index()
print("\n",sales_by_genre)

#calcular el top 5
top_publishers = df.groupby("Publisher")["Global_Sales"].sum().nlargest(5).reset_index()
print("\n",top_publishers)

# ventas consola
ventas_consola = df.groupby("Platform") ["Global_Sales"].sum().nlargest(10).reset_index()
print("\n",ventas_consola)

# ventas pbllisher
ventas_consola = df.groupby("Publisher") ["JP_Sales"].sum().nsmallest(10).reset_index()
print("\n",ventas_consola)


print ("\n\n-------------------------------EXAMEN---------------------------------")

print ("\nJuegos menos vendidos por nombre y plataforma")

juegosmenosv_nombreyplataforma = df.groupby(["Name","Platform"]) ["Global_Sales"].sum().nsmallest(10).reset_index()
print("\n",juegosmenosv_nombreyplataforma)


print ("\nJuegos menos vendidos por plataforma")

juegosmenosv_plataforma = df.groupby("Platform") ["Global_Sales"].sum().nsmallest(10).reset_index()
print("\n",juegosmenosv_plataforma)


print ("\nJuegos más vendidos por nombre y género")

juegosmasv_nombreygen = df.groupby(["Name","Genre"]) ["Global_Sales"].sum().nlargest(10).reset_index()
print("\n",juegosmasv_nombreygen)