import requests
import json

headers = {"Content-Type": "application/json"}
data = json.dumps({"postcodes": ["OX49 5NU", "M32 0JG, NE30 1DP"]})
r = requests.post(
    url="https://api.postcodes.io/postcodes/",
    headers=headers,
    data=data
)
result = r.json()
print(r.json())

print(result['result']['admin_district'])
#['parlimentary_constituency']

#     print(result['result']['eastings'], result['result']["northings"])

#for each postcode, print PostCode: region, parlimentary_constituency


#r = requests.get("https://api.postcodes.io/postcodes/SE120NB")

#print(r)
#
# if r.status_code == 200:
#     content = r.content
#     #print(content)
#     result = r.json()
#






#print(post_codes_req.status_code)

# #print(post_codes_req.content)
# #print(post_codes_req.json())
# print(post_codes_req)