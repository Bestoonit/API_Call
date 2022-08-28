
import requests
import csv

number_of_servers = int(input("Number of Servers: "))
def asset_creation():

    # Creating a static list of Keys for the payload dictionary keys, key:value for the header and an empty dictionary for creating the payload.
    itemkeys = ["clientType", "computerType", "description", "owner", "region",  "subOU", "companyCode", "adminGroupApprover", "adminGroupOwner", "functionalDescription", "organisationalUnit"]
    payload = {}
    header = {"Autherization": "Some_token"}
    
    #Dynamic User inputs      
    clientType = input('clientType: ') #required string 
    description = input("description: ")
    owner = input("owner: ")
    region = input("region: ")
    subOU = input("subOU: ") 
    
    #Static User input
    computerType = "server"
    companyCode = ""
    adminGroupApprover = ""
    adminGroupOwner = ""
    functionalDescription = ""
    organisationalUnit = ""

    #populating payload dictionary with the key from itmekeys and values from the user's input
    input_values = [clientType, computerType, description, owner, region, subOU, companyCode, adminGroupApprover, adminGroupOwner, functionalDescription, organisationalUnit]
    for value in range(len(input_values)):
        payload[itemkeys[value]] = input_values[value]

    #sending post request with the payload and saving the response as a dicutionary
    url = "https://httpbin.org/post"
    r = requests.post(url, data=payload, headers=header, timeout=10) #timeout for 10 second
    print(r)
    print(r.text)
    r_dict = r.json()

    #Saving the specific values in a list
    list_values = []
    for values in itemkeys:
        list_values.append((r_dict["form"][values]))
    print(list_values)

    #Saving the list to a CSV file
    with open('computer_Name.csv', 'a', newline='') as csvfile:
        csv_creator = csv.writer(csvfile)
        csv_creator.writerow(list_values)



for number in range(number_of_servers):
    asset_creation()


