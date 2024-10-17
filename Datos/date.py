import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Datos/poblacion.csv")

print(df)

x= (df["Date"])
y= (df["JPN"])
z= (df["HRV"])
t= (df["COL"])

plt.plot(x,y)
plt.plot(x,z)
plt.plot(x,t)
plt.xlabel("Fecha")
plt.ylabel("Poblacion")
plt.title("Grafico de barras de Matplotlib")
plt.show()

# filtro = df[df["COL"]>30000000]
# print(filtro["COL"])
# print(df.head())
#print(df.describe())
# print(df.tail())
# print(df.sample())