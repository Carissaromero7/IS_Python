#deniro_pd.py
#Written by: Carissa Romero

import pandas as pd 

#read in csv file 
df = pd.read_csv("deniro.csv", quotechar='"',skipinitialspace=True)
                     
#print the score for Heat
print(df[df["Title"].str.contains("Heat")])

#print all the movies from 1992
print(df[df["Year"].isin([1992])])

