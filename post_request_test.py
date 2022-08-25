import requests
import csv

itemlist = ["clientType", "computerType", "description", "owner", "region"]
payload = {}

clientType = input('clientType ex.( "Desktops" "Laptops" ): ') 
computerType = input("computerType (Workstation, Server): ") 
description = input("description: ") 
owner = input("owner: ") 
region = input("region: ") 

payload[itemlist[0]] = clientType
payload[itemlist[1]] = computerType
payload[itemlist[2]] = description
payload[itemlist[3]] = owner
payload[itemlist[4]] = region

url = "https://httpbin.org/post"
r = requests.post(url, data=payload)
r_dict = r.json()

list_values = []
for values in itemlist:
    list_values.append((r_dict["form"][values]))


with open('computer_Name.csv', 'a', newline='') as csvfile:
   csv_creator = csv.writer(csvfile)
   csv_creator.writerow(list_values)
