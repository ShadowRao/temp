import requests
import json
API_ENDPOINT="http://172.20.3.125:5000"
DELIVERY_INFO=f"{API_ENDPOINT}/DeliveryInfo"
HEADER_DICT={"Content-Type":"application/json"}

lit=["00010242fe8c5a6d1ba2dd792cb16214", 
"00018f77f2f0320c557190d7a144bdd3", 
"000229ec398224ef6ca0657da4fc703e", 
"00024acbcdf0a6daa1e931b038114c75", 
"00042b26cf59d7ce69dfabb4e55b4fd9", 
"00048cc3ae777c65dbb7d2a0634bc1ea", 
"00054e8431b9d7675808bcb819fb4a32", 
"000576fe39319847cbb9d288c5617fa6", 
"0005a1a1728c9d785b8e2b08b904576c", 
"0005f50442cb953dcd1d21e1fb923495", 
"00061f2a7bc09da83e415a52dc8a4af1", 
"00063b381e2406b52ad429470734ebd5", 
"0006ec9db01a64e59a68b2c340bf65a7", 
"0008288aa423d2a3f00fcb17cd7d8719", 
"0008288aa423d2a3f00fcb17cd7d8719", 
"0009792311464db532ff765bf7b182ae", 
"0009c9a17f916a706d71784483a5d643", 
"000aed2e25dbad2f9ddb70584c5a2ded", 
"000c3e6612759851cc3cbb4b83257986", 
"000e562887b1f2006d75e0be9558292e", 
"000e63d38ae8c00bbcb5a30573b99628"]
for i in range(len(lit)):
	REQUEST_DATA_DICT={"order_id":lit[i]}

	RESPONSE_OBJ=requests.post(url=DELIVERY_INFO,headers=HEADER_DICT,json=REQUEST_DATA_DICT)

	print(json.dumps(RESPONSE_OBJ.json(),indent=4))
	print(RESPONSE_OBJ.status_code)




