#datapoints1.py
#Written by: Carissa Romero
#Date: 7/21/19
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv") #read in titanic data
df1 = df[df["Sex"] == "male"] #filter data by male 
df2 = df[df["Sex"] == "female"] #filter data by female
#print(df.head)

x1 = df1["Age"] #filter male data by Age 
y1 = df1["SibSp"] #filter male data by Sibsp

x2 = df2["Age"]  #filter female data by Age
y2 = df2["SibSp"] #filter female data by SibSp

y3 = df1["Parch"]  #filter male data by Parch

y4 = df2["Parch"] #filter female data by Parch

fig, ax = plt.subplots(ncols=2,nrows=2,figsize=(6,6)) #create a 2x2 plot

ax[0,0].scatter(x1,y1, s=5, marker='o')
ax[0,0].set_xlabel("Age")
ax[0,0].set_ylabel("Number of Siblings/Spouses")
ax[0,0].set_xlim(-3,103)
ax[0,0].set_ylim(-.20,5.20)
ax[0,0].set_xticks([0,25,50,75,100])
ax[0,0].set_yticks([0,1,2,3,4,5])
ax[0,0].set_title("Male SibSp")

ax[0,1].scatter(x2,y2,s=5, marker='o')
ax[0,1].set_xlabel("Age")
ax[0,1].set_ylabel("Number of Siblings/Spouses")
ax[0,1].set_xlim(-3,103)
ax[0,1].set_ylim(-.20,5.20)
ax[0,1].set_xticks([0,25,50,75,100])
ax[0,1].set_yticks([0,1,2,3,4,5])
ax[0,1].set_title("Female SibSp")

ax[1,0].scatter(x1,y3,s=5, marker='o')
ax[1,0].set_xlabel("Age")
ax[1,0].set_ylabel("Number of Parents/Children")
ax[1,0].set_xlim(-3,103)
ax[1,0].set_ylim(-.20,6.20)
ax[1,0].set_xticks([0,25,50,75,100])
ax[1,0].set_yticks([0,2,4,6])
ax[1,0].set_title("Male Parch")

ax[1,1].scatter(x2,y4,s=5, marker='o')
ax[1,1].set_xlabel("Age")
ax[1,1].set_ylabel("Number of Parents/Children")
ax[1,1].set_xlim(-3,103)
ax[1,1].set_ylim(-.20,6.20)
ax[1,1].set_xticks([0,25,50,75,100])
ax[1,1].set_yticks([0,2,4,6])
ax[1,1].set_title("Female Parch")

plt.subplots_adjust(hspace=0.5) #create a space between the top two plots and the bottom two plots
plt.show()