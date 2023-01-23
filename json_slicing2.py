import json
import requests

url = ("https://jsonplaceholder.typicode.com/posts")
response = requests.get(url)

'''Converting data into json format'''
data = response.json()

'''with open method no need to close the file 
file will be automatically closed'''

with open("first_twenty.json", "w") as file:
    json.dump(data[0:20], file, indent = 3)    
