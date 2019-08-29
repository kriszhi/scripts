import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=AWS instance shutdown successfully&language=english&route=p&numbers=9080108716,9941699930"
headers = {
'authorization': "xxxxx",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)