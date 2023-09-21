import psycopg2
import requests
import json
API_ENDPOINT="http://172.20.3.125:5000"
DELIVERY_INFO=f"{API_ENDPOINT}/DeliveryInfo"
HEADER_DICT={"Content-Type":"application/json"}
lit=[]
#establishing the connection
conn = psycopg2.connect(
   database="amazon", user='workshop_user', password='workshop_user1', host='172.20.3.125', port= '5435'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
cursor.execute("SELECT order_id FROM order_items")
for row in cursor.fetchall():
	
	#Executing an MYSQL function using the execute() method
	#cursor.execute("SELECT order_id FROM order_items")

	# Fetch a single row using fetchone() method.
	
	line=(str(row[0]))
	
	
	REQUEST_DATA_DICT={"order_id":line}
	
	RESPONSE_OBJ=requests.post(url=DELIVERY_INFO,headers=HEADER_DICT,json=REQUEST_DATA_DICT)

	print(json.dumps(RESPONSE_OBJ.json(),indent=4))
	print(RESPONSE_OBJ.status_code)
	
#Closing the connection
conn.close()
