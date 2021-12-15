#Letra G
import pandas as pd 
Titanic = pd.read_csv("titanic.csv")

auxTitanic = Titanic.loc[Titanic["Survived"]== 1]
Titanic = Titanic.groupby(['Survived','Pclass']).count()
print(auxTitanic)
