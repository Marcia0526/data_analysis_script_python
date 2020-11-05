# coding=gbk
import requests
import pandas as pd
import numpy as np

headers = {"X-Authorization": "mpRER92-HgeYj*R9avmX"}
url = "https://us-central1-revenue-forecast-accuracy.cloudfunctions.net/u-api-prod/employees"
response = requests.get(url=url, headers=headers).json()
response = response['data']
filtered_response = []
print('original length:' + str(len(response)))
for entry in response:
    if entry is not None:
        filtered_response.append(entry)
# print(filtered_response)
print('current length:' + str(len(filtered_response)))

api_employee_info = pd.DataFrame(filtered_response)
# api_employee_info.to_csv(r'/Users/jingcai/Downloads/api_employee_info.csv')


excel_employee_info = pd.read_excel(r'/Users/jingcai/Downloads/excel_employee_info.xlsx')
excel_employee_info = pd.DataFrame(excel_employee_info)

api_employee_info = pd.read_csv(r'/Users/jingcai/Downloads/api_employee_info.csv')

compare_result = pd.merge(api_employee_info, excel_employee_info, how='right', on='employeeId')

compare_result = pd.DataFrame(compare_result)


def function(a, b):
    if a == b:

        return 1

    else:

        return 0


compare_result['bool'] = compare_result.apply(lambda x: function(x['unitName_x'], x['unitName_y']), axis=1)

compare_result.to_csv(r'/Users/jingcai/Downloads/compare_result.csv')
