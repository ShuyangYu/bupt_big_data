import pandas as pd
import numpy as np
import gc
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid", color_codes=True)

# headers
headers_student_info = ['id', 'sex', 'grade', 'school', 'province']
headers_student_network_record = ['id', 'logintime', 'logouttime', 'in_mb', 'out_mb', 'user_mac', 'user_os']
headers_consume_record = ['id', 'day', 'time', 'remainder', 'type']

# load data
by_student_info_data = pd.read_csv('by/by_student_info.csv', sep='\t', names=headers_student_info)
by_student_network_record_data = pd.read_csv('by/by_student_network_record.csv', sep='\t', names=headers_student_network_record).drop(['user_mac', 'user_os'], axis=1)

# merge network with info
network_info_data = pd.merge(by_student_network_record_data,by_student_info_data, on='id')

# 更改grade与logintime/logouttime的格式
network_info_data['grade'] = network_info_data['grade'].astype('int')
network_info_data['logintime'] = pd.to_datetime(network_info_data['logintime'])
network_info_data['logouttime'] = pd.to_datetime(network_info_data['logouttime'])

# 需删除行数
del_rows = []

for i in range(network_info_data.shape[0]):
    if((network_info_data['logintime'].iloc[i] < pd.Timestamp(network_info_data['grade'].iloc[i], 8, 31, 23, 59, 59)) or (network_info_data['logintime'].iloc[i] > pd.Timestamp(network_info_data['grade'].iloc[i] + 1, 7, 31, 23, 59, 59))):
        del_rows.append(i)
    if(i % 1000000 == 0):
        print(i)

grade_one_network_info_data = network_info_data.drop(del_rows, axis=0)   
grade_one_network_info_data.to_csv('grade_one_network_info_data.csv') 

del grade_one_network_info_data, network_info_data
gc.collect()

# merge consume with info
by_student_consume_record_data = pd.read_csv('by/by_student_consume_record.csv', sep='\t', names=headers_consume_record)
consume_student_info_data = pd.merge(by_student_consume_record_data,by_student_info_data, on='id')

# 处理缺失值
consume_student_info_data = consume_student_info_data.dropna(axis = 0)

# 添加datetime列
consume_student_info_data['datetime'] = pd.to_datetime(consume_student_info_data['day'] + ' ' + consume_student_info_data['time'])
consume_student_info_data['grade'] = consume_student_info_data['grade'].astype('int')

# 删除行数
del_rows = []
for i in range(consume_student_info_data.shape[0]):
    if((consume_student_info_data['datetime'].iloc[i] < pd.Timestamp(consume_student_info_data['grade'].iloc[i], 8, 31, 23, 59, 59)) or (consume_student_info_data['datetime'].iloc[i] > pd.Timestamp(consume_student_info_data['grade'].iloc[i] + 1, 7, 31, 23, 59, 59))):
        del_rows.append(i)
    if(i % 1000000 == 0):
        print(i)

new_consume_student_info_data = consume_student_info_data.reset_index().drop(labels=del_rows, axis=0)
new_consume_student_info_data.to_csv('consume_info_data_data.csv')