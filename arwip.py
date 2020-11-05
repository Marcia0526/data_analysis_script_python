import pandas as pd
regional = pd.read_excel(r'/Users/jingcai/Downloads/TW_DSO_AR_WIP.xlsx',names=['year','ledger','project_code','value','type','currency']);
# 查看行列
print(regional.shape);
# 查看缺失值
# print(regional.info);
# 删除缺失值
regional_handle = regional.dropna();
regional_handle['project_code_year']=regional_handle['project_code']+regional_handle['year'].to_string();
# print(regional_handle.shape);
print(regional_handle.iloc[0:2]);#选择打印前三行
initial_table = pd.read_excel(r'/Users/jingcai/Downloads/dso_test_dso_ar_wip_initial.xlsx');
print(initial_table.shape);

result=pd.merge(regional,initial_table, on=['project_code','year'],how='left');
print(result.shape);
print(result);

