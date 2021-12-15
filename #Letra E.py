#Letra E
import pandas as pd 
Titanic = pd.read_csv("titanic.csv")

Titanic.rename(columns={'PassengerId':'ID_Passageiro'}, inplace = True)
Titanic.rename(columns={'Pclass':'Classe'}, inplace = True)
Titanic.rename(columns={'Sex':'Sexo'}, inplace = True)
Titanic.rename(columns={'Name':'Nome'}, inplace = True)
Titanic.rename(columns={'Age':'Idade'}, inplace = True)
Titanic.rename(columns={'Cabin':'Cabine'}, inplace = True)
Titanic.rename(columns={'Fare':'Tarifa'}, inplace = True)
Titanic.rename(columns={'Embarked':'Embarque'}, inplace = True)
print(Titanic)

