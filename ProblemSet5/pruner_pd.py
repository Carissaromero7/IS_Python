#pruner_pd.py
#Written by: Carissa Romero
#10/14/19

import pandas as pd 

import json

with open("baby_names.txt") as infile: 

	data = json.load(infile)

	data1 = data["top"].items() # need the data within the subkey "top"

    #storing the data in a pandas Dataframe
	df = pd.DataFrame(data1, columns = ["Name", "Count"]) # create column headers

	df1 = df[~df["Name"].str.contains("v")] #remove all names with the letter v

	df2 = df1[~df1["Count"].str.contains("28")] #remove names with count of 28

	delnames = ["Gary","Aaron","Luke","Winston","Avery"] 

	df3 = df2[~df2["Name"].str.contains("|".join(delnames))] #remove all instance of the above list

	df4 = pd.DataFrame([["Ron", 5]], columns=["Name", "Count"]) # add the name Ron with a count of 5

	df5=df3.append(df4, ignore_index=True)

print(df5) #print the DataFrame
