import pandas as pd
import yaml
import os


def read_file(file_name):
    current_path = os.path.dirname(__file__) + '/input_output_file_name.yml'
    with open(current_path, 'r') as f:
        properties = yaml.load(f.read(), yaml.SafeLoader)
    return properties[file_name]


# 读取并处理people表的数据
people_data = pd.read_excel(read_file('people_file'))
people_data['people_total'] = people_data['has_taken'] + people_data['left_vacation']

# 读取leave的数据
leave_data = pd.read_excel(read_file('leave_file'))
leave_data['leave_total'] = leave_data['takenUntilToday'] + leave_data['leftUntilEndOfYear']

# 剔除type=sick leave
leave_data = leave_data[leave_data['type'].isin(['Annual Leave'])]

# 连接people表和leave表
people_leave_merge = pd.merge(people_data, leave_data, how='left', on='employeeId')

# 计算差值
people_leave_merge['gap'] = (people_leave_merge['people_total'] - people_leave_merge[
    'leave_total']).abs()

# # 剔除入职时间不一致的数据
# diff_start_time = pd.read_excel(read_file('diff_start_time'))
# people_leave_merge = people_leave_merge[~people_leave_merge['employeeId'].isin(diff_start_time['employeeId'])]

people_leave_merge.to_csv(read_file('compare_leave_output_file'))


# # 剔除rehire+转正 & contractor
# rehire_data = pd.read_excel('r'+read_file('rehire_contractor_file'))
# people_leave_merge = people_leave_merge[~people_leave_merge['employeeId'].isin(rehire_data['employeeId'])]
#
# # 剔除上一年的余额
# last_left = pd.read_excel('r'+read_file('last_year_left'))
# people_leave_merge = people_leave_merge[~people_leave_merge['employeeId'].isin(last_left['employeeId'])]
# people_leave_merge = people_leave_merge[people_leave_merge['gap'] > 0.5]



# people_last_leave = pd.read_excel(read_file('last_year_left'))
# leave_rehire = pd.read_excel(read_file('leave_rehire_date'))
# people_leave = pd.merge(people_last_leave, leave_rehire, how='left', on='employeeId')
# # people_leave_rehire['gap'] = pd.DataFrame(pd.to_datetime(
# #     people_leave_rehire['originalServiceStartDate']) - pd.to_datetime(people_leave_rehire['Original Start Date']))
#
# people_leave['gap']=people_leave['leaveCarryFromLastYear']-people_leave['last_year']
# people_leave.to_csv(read_file('compare_leave_people'))

