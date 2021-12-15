import pandas as pd 
import matplotlib.pyplot as plt

#Letra A
Titanic = pd.read_csv("titanic.csv")
#print(Titanic.head(10))

#Letra B
NomeEmOrdem = Titanic.sort_values('Name')
print("Em ordem alfabetica:")
#print(NomeEmOrdem.head(10))  
    
#Letra C
Titanic['Sobreviventes']=Titanic['Survived']
Titanic['Sobreviventes']=Titanic['Sobreviventes'].replace([1],'Sim')
Titanic['Sobreviventes']=Titanic['Sobreviventes'].replace([0],'Não')

#Letra D
Titanic.drop('SibSp', axis = 1 , inplace= True)
Titanic.drop('Parch', axis = 1 , inplace= True)
Titanic.drop('Ticket',axis = 1 , inplace= True)

#Letra E
Titanic.rename(columns={'PassengerId':'ID_Passageiro'}, inplace = True)
Titanic.rename(columns={'Pclass':'Classe'}, inplace = True)
Titanic.rename(columns={'Sex':'Sexo'}, inplace = True)
Titanic.rename(columns={'Name':'Nome'}, inplace = True)
Titanic.rename(columns={'Age':'Idade'}, inplace = True)
Titanic.rename(columns={'Cabin':'Cabine'}, inplace = True)
Titanic.rename(columns={'Fare':'Tarifa'}, inplace = True)
Titanic.rename(columns={'Embarked':'Embarque'}, inplace = True)

#Letra F
Titanic['Sexo']= Titanic['Sexo'].replace(['male','female'],['masculino','FEMININO'])
Titanic['Sexo']= Titanic['Sexo'].replace(['male'],['masculino'])
Titanic['Sexo']= Titanic['Sexo'].replace(['female'],['FEMININO'])

#Letra G
auxTitanic = Titanic.loc[Titanic["Survived"]== 1]
auxTitanic = Titanic.groupby(['Survived','Pclass']).count()
print(auxTitanic)

#Letra H
auxTitanic = Titanic.loc[Titanic["Survived"]== 1]
auxTitanic = Titanic.groupby(['Survived','Sex']).count()
print(auxTitanic)

#Letra I
print(Titanic[['Survived','male']])
plt.bar(Titanic['Survived'],Titanic['male'])
plt.xticks(rotation=90)
plt.show()

#Letra J




