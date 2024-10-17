import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[11,44,50,45]
mylavels=["naranjas","peras","verduras","bananas"]

plt.pie(y,labels = mylavels)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Grafico simple de Matplotlib")
plt.show()