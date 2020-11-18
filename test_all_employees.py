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

print(access_token)

headers = {
    "Authorization": access_token,
}
params = {
    "active": "yes",
    "country": "CHN"
}
url = "https://apistg.thoughtworks.net/people/v2/employees"
response = requests.get(url=url, headers=headers, params=params).json()
print("-------")
print(response)
handled_response = []
num_null = 0
for entry in response:
    if entry is not None:
        handled_response.append(entry)
    else:
        num_null += 1

all_employee_info = pd.DataFrame(handled_response)
print(num_null)
print(all_employee_info.head(5))
print(all_employee_info.shape[0])
all_employee_info.to_csv(r'/Users/jingcai/Downloads/all_employee_info.csv')

test_employee_info = pd.read_excel(r'/Users/jingcai/Downloads/workday employee spreadsheet.xlsx',
                                   squeeze=False)
print(test_employee_info.shape[0])

# diff_actual_test = pd.merge(all_employee_info, test_employee_info, how='left', on='employeeId')


# diff_actual_test.to_csv(r'/Users/jingcai/Downloads/diff_actual_test.csv')
