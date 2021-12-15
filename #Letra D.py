#Letra D
import pandas as pd 
Titanic = pd.read_csv("titanic.csv")

Titanic.drop('SibSp', axis = 1 , inplace= True)
Titanic.drop('Parch', axis = 1 , inplace= True)
Titanic.drop('Ticket',axis = 1 , inplace= True)
print(Titanic)