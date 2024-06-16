#Programming with Arshil Noor
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn import linear_model
df=pd.read_excel("C:\\Users\\पज\\Desktop\\Office\\5. Even Sem (2023-24)\\B.Tech [Third Year CS (6th Sem)]\\Practical (DA)\\Price.xlsx")
reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.Price)


plt.xlabel('area(sqr ft)')
plt.ylabel('price(Rs.)')
plt.scatter(df.area,df.Price, color='red', marker='+')
plt.plot(df.area,reg.predict(df[['area']]),color='blue')
plt.show() 