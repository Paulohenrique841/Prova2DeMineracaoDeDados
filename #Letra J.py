#Letra J
import pandas as pd 
Titanic = pd.read_csv("titanic.csv")

Titaexcel=pd.ExcelWriter('Titanicexcel.xlsx')
Titanic.to_excel(Titaexcel, index = False)
Titaexcel.save()
