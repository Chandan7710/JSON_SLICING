import json
import requests

url = ("https://jsonplaceholder.typicode.com/posts")
response = requests.get(url)

'''Converting data into json format'''
data = response.json()

file = open("twenty_items.json", "w")
'''dumping data into json file using indentation'''
json.dump(data[0:20], file, indent = 3)
file.close()
