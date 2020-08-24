#pruner.py
#Created by: Carissa Romero
#Date: 10/9/2019

import json #need in order to make a JSON file

selectedkeys = [] #create an empty list
#want to remove names "Gary", "Aaron", "Luke", "Winston", "Avery"
delnames= ["Gary", "Aaron", "Luke", "Winston", "Avery"]
with open("baby_names.txt") as infile: 
    data = json.load(infile) #reading in a JSON file 
    for name in data["top"]: #need to get into the subkey of the dict
        if "v" in name or name in delnames: #want to remove all names that contain the letter "v" or are in the list "delnames" 
            selectedkeys.append(name) #add these names to the list you created
    		#print(selectedkeys)

    for (name, value) in data["top"].items():
        if value == "28": #want to remove names with a count of 28
            selectedkeys.append(name) #add these names to the list you created
            #print(selectedkeys)

    for name in selectedkeys: 
        if name in data["top"]: 
    # if the names are in the list "selected keys" delete the names
            del data["top"][name]

    data["top"].update({"Ron": "5"}) #add the name "Ron" with a count of 5
   #write the resulting dictionary in JSON format in a file
with open("better_names.txt","w") as outfile:
    json.dump(data, outfile, indent=4) #indent=4 for easier reading
