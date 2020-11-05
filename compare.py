import pandas as pd
from pandas import DataFrame

df_sf = pd.read_csv(r'/Users/jingcai/Downloads/sf.csv',
                    names=['id', 'opportunity_id', 'actual_revenue', 'CURRENCY_CD', 'YEAR', 'MONTH',
                           'office'])  # 打开文件salesforce同步数据,并给文件加title
print(df_sf)

df_project = pd.read_csv(r'/Users/jingcai/Downloads/ProjectCode.csv',
                         names=['opportunity_id', 'PROJECT_ID']) # 打开opportunity——id与project-id映射表
print(df_project)

df_current_prod = pd.merge(df_sf, df_project, how='left', on='opportunity_id')  # 将上述两表关联起来
print(df_current_prod)

df_pretti = pd.read_excel(r'/Users/jingcai/Downloads/pretti.xlsx')
print(df_pretti)

df_merge_result = pd.merge(df_current_prod, df_pretti, how='right', on=['PROJECT_ID', 'CURRENCY_CD', 'YEAR', 'MONTH'])
print(df_merge_result)
df_merge_result.to_csv(r'/Users/jingcai/Downloads/merge_result.csv')

df_merge_result['sum_money'] = df_merge_result['actual_revenue'] + df_merge_result['SUM(L.MONETARY_AMOUNT)']
print(df_merge_result)

df_merge_result.to_csv(r'/Users/jingcai/Downloads/compare_result.csv')
