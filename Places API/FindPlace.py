import requests

url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=cabeamento%20estruturado&inputtype=textquery&fields=formatted_phone_number%2name%2geometry&key=AIzaSyABEQ7SN-jsgy_YnQDOizet_VK0xFSwJ_w"

payload= {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
