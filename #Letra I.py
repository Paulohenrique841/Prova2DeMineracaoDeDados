#Letra I
import pandas as pd 
import matplotlib.pyplot as plt

Titanic = pd.read_csv("titanic.csv")

print(Titanic[['Survived','male']])
plt.bar(Titanic['Survived'],Titanic['male'])
plt.xticks(rotation=90)
plt.show()