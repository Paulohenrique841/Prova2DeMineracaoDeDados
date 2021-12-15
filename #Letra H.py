#Letra H
import pandas as pd 
Titanic = pd.read_csv("titanic.csv")


auxTitanic = Titanic.loc[Titanic["Survived"]== 1]
auxTitanic = Titanic.groupby(['Survived','Sex']).count()
print(auxTitanic)