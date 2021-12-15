#Letra F
import pandas as pd 
Titanic = pd.read_csv("titanic.csv")

Titanic['Sexo']= Titanic['Sexo'].replace(['male','female'],['masculino','FEMININO'])
Titanic['Sexo']= Titanic['Sexo'].replace(['male'],['masculino'])
Titanic['Sexo']= Titanic['Sexo'].replace(['female'],['FEMININO'])
print(Titanic)

