import pandas as pd

employee_all = pd.read_excel(r'/Users/jingcai/Downloads/归属查询名单 (1).xlsx',
                             sheet_name='总表',
                             usecols=['HomeOffice', 'employeeId', 'ChineseName', '员工类型'],
                             squeeze=False
                             )
employee_LTA = employee_all[employee_all['员工类型'].isin(['LTA'])]
print(employee_LTA.head(5))
print(employee_LTA.shape[0])
print(employee_LTA.shape[1])

diff_timecard_leave = pd.read_excel(r'/Users/jingcai/Downloads/EntryTimeCardMisMatch.xlsx',
                                    squeeze=False)

LTA_timecard_leave = pd.merge(employee_LTA, diff_timecard_leave, how='left', on='employeeId')

print(LTA_timecard_leave)

LTA_timecard_leave.to_csv(r'/Users/jingcai/Downloads/LTA_timecard_leave.csv')
