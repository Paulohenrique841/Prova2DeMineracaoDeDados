#Letra C
import pandas as pd 
Titanic = pd.read_csv("titanic.csv")


Titanic['Sobreviventes']=Titanic['Survived']
Titanic['Sobreviventes']=Titanic['Sobreviventes'].replace([1],'Sim')
Titanic['Sobreviventes']=Titanic['Sobreviventes'].replace([0],'Não')
print(Titanic)