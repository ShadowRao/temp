# Requesting API example

## How to make a sample API request using python script.
Copy & paste the below code and run the python script.
```
import requests
import json

# This is the post API URL, use DeliveryInfo/ProductStats
url = 'http://127.0.0.1:5000/DeliveryInfo'
headers = {"Content-Type": "application/json"}

# Use the post data to make requests based on the API
post_data = {'order_id': '47770eb9100c2d0c44946d9cf07ec65d'}

# Use requets library to invoke a request
r = requests.post(
    url=url,
    headers=headers,
    data=json.dumps(post_data))
    
# print the response
print(json.dumps(r.json(), indent=4))
```
