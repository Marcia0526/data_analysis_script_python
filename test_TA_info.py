import requests
import pandas as pd

auth_headers = {
    "Authorization": "",
    "Content-Type": "application/x-www-form-urlencoded"
}

auth_data = {
    "grant_type": "",
    "scope": ""
}

auth_url = ""

auth_response = requests.post(url=auth_url, headers=auth_headers, data=auth_data).json()
access_token = "Bearer " + auth_response['access_token']

headers = {
    "Authorization": access_token
}
url = "https://apistg.thoughtworks.net/china-unit/units"
response = requests.get(url=url, headers=headers).json()
print(response)
response = response['data']
handled_response = []
for entry in response:
    if entry is not None:
        handled_response.append(entry)
actual_TA_info = pd.DataFrame(handled_response)
print(actual_TA_info.head(5))
print(actual_TA_info.shape[0])
test_TA_info = pd.read_excel(r'/Users/jingcai/Downloads/U&TA spreadsheet.xlsx')
print(test_TA_info.shape[0])
