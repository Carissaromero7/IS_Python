#survival.py
#Written by: Carissa Romero
#Date: 10/21/19

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("train.csv")#read in data from CSV file

df= df[df["Survived"] == 1]#filter by those who survived
df.dropna(subset= ["Age"]) #drop all data points that do not have an Age 

#print(df.info)
df1 = df[df["Sex"] == "male"] #filter by male 
df2 = df[df["Sex"] == "female"]#fiter by female
#print(df1.info)
 
x1= df1["Age"] #age of Males who survived 
x2= df2["Age"] #age of Females who survived

range = (0,100) #range of ages
bins = 10 

#plot both histograms together 
plt.hist([x1,x2],bins,range,rwidth=.4,align="right",label=["Male","Female"]) 
#align = "right" -- bars are centered on the right bin edges

plt.xlabel("Age")
plt.ylabel("Count")

plt.xticks([10,20,30,40,50,60,70,80,90,100])
plt.yticks([0,10,20,30,40,50])
plt.legend() 
plt.title("Survival by Age and Gender")
plt.show()
