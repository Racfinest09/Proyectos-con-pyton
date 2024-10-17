import pandas as pd
lista=[1,2,3,4,5,6,7,8,9,10]
labels=["a","b","c","d","e","f","g","h","i","j"]
print(lista)
#crear una serie
mi_serie =pd.Series(lista,labels)
print(mi_serie)
