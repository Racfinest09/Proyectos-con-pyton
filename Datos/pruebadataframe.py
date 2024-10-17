import pandas as pd

#crear un data frame
nombre =["Ana","Luis","Oscar"]
edad =[23,45,12]
telefono =[3214565456,3214569766,315678943]
data={"nombre":["Ana","Oscar","Juan"],"edad":[23,31,59],"telefono":[3214567890,3224098756,3143503476]}
df= pd.DataFrame(data)
print(df)
data2 = pd.DataFrame([nombre,edad,telefono])
print(data2)
df.to_csv("salida.csv", index=False)