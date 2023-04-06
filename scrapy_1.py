import requests
import json
import csv

# setting input value
FromData = input("Enter FromData:")
EndData = input("Enter EndData:")
InputType = input("Did you scrapy start from 1(y or n):")
if InputType == 'n':
    DocketNumber = input("Please index of ID:")

print("Please wait a few minutes while doing data scrapy.")

# csv file header
fieldnames = ['Docketname', 'Data Stored', 'Document_Name', 'Link to Document']

# data scrapy
url = 'https://oitco.hylandcloud.com/DNRCOGPublicAccess/api/CustomQuery/KeywordSearch'
data = {'QueryID': 179, 'keywords': [],'FromDate':FromData, 'ToDate': EndData, 'QueryLimit':0}

proxies = {"http" : "http://adamoilandgas:FKJLR9ED599UHX2XU0L2GCI0@138.128.46.175:11665"}

response = requests.post(url, data=data, proxies=proxies)

res_data = response.json()

# save result of csv file
output_array = []

print("Data Scrapy is finish")

# setting start and end value
if InputType == 'y':
    start_docket = 1
    end_docket = 999999999
elif InputType == 'n':
    start_docket = int(DocketNumber)
    end_docket = 999999999

# data scrapy in range
for index_docket in range(start_docket,end_docket):
    str_index = str(index_docket)
    count = 0
    for i in res_data['Data']:
        sub_res_data = i['DisplayColumnValues']
    
        item = sub_res_data[1]
        item_value = item['Value']


        if str_index in item_value:
            id = i['ID']

            first_item = sub_res_data[0]
            store_data = first_item['Value']
            Docuement_name = item_value
            url = "https://oitco.hylandcloud.com/DNRCOGPublicAccess/api/Document/"+id
        
            output_item ={
                 'Docketname' : index_docket,
                 'Data Stored' : store_data,
                 'Document_Name' : Docuement_name,
                 'Link to Document' : url}
            output_array.append(output_item)
            count = count + 1
            
    print(index_docket,"count = ", count)

# save data to csv file
with open('example.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(output_array)

print("The end")
        
