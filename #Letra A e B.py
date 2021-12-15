#Letra A e B
import pandas as pd 
Titanic = pd.read_csv("titanic.csv")

#Letra A
Titanic = pd.read_csv("titanic.csv")
print(Titanic.head(10))

#Letra B
NomeEmOrdem = Titanic.sort_values('Name')
print("Em ordem alfabetica:")
print(NomeEmOrdem.head(10))  
    