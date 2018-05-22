# coding: utf-8
import gc

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set(style="whitegrid", color_codes=True)

# headers
# headers_by_student_network_record = ['id', 'logintime', 'logouttime', 'in_mb', 'out_mb', 'user_mac', 'user_os']
# headers_by_student_info = ['id', 'sex', 'grade', 'school', 'province']
# headers_by_course_schedule_info = ['id', 'name', 'teacher', 'classroom', 'start_class', 'stop_class', 'class_week', 'class_weekday', 'year', 'term']

# load data
# by_student_network_record_data = pd.read_csv('by/by_student_network_record.csv', sep='\t', names=headers_by_student_network_record).drop(['user_mac', 'user_os'], axis=1)
# by_student_info_data = pd.read_csv('by/by_student_info.csv', sep='\t', names=headers_by_student_info)
# by_course_schedule_info_data = pd.read_csv('by/by_course_schedule_info.csv', sep='\t', names=headers_by_course_schedule_info)

# by_student_network_record_data = pd.read_csv('new_network_student_info_data.csv')

# print(by_student_network_record_data.head())

# # 取出logintime的年/月/日
# by_student_network_record_data['day'] = by_student_network_record_data['logintime'].str.split(expand=True)[0]
# # 更改logintime和logouttime的格式
# by_student_network_record_data['logintime'] = pd.to_datetime(by_student_network_record_data['logintime'])
# by_student_network_record_data['logouttime'] = pd.to_datetime(by_student_network_record_data['logouttime'])
# # 计算总流量
# by_student_network_record_data['total_mb'] = by_student_network_record_data['in_mb'] + by_student_network_record_data['out_mb']
# # 取出logintime的weekday
# by_student_network_record_data['weekday'] = by_student_network_record_data['logintime'].dt.weekday
# # 计算每个logintime和logouttime的时间差，并通过total_seconds转换为小时
# by_student_network_record_data['duration'] = by_student_network_record_data['logouttime'] - by_student_network_record_data['logintime']
# by_student_network_record_data['duration_seconds'] = (by_student_network_record_data['duration'].dt.total_seconds()) / 3600.
# # 吧logintime转换为小时
# by_student_network_record_data['logintime_seconds'] = (by_student_network_record_data['logintime'].dt.hour * 3600. + by_student_network_record_data['logintime'].dt.minute * 60 + by_student_network_record_data['logintime'].dt.second) / 3600.

# 得到每个人每天的上网次数，按id，logintime排序
# 处理跨天数据，截止到23：59：59
# by_student_network_record_data = by_student_network_record_data.sort_values(by=['id', 'logintime']).reset_index()

# for i in range(by_student_network_record_data.shape[0]):
#     if(by_student_network_record_data['logintime'][i].day != by_student_network_record_data['logouttime'][i].day):
#         by_student_network_record_data['logouttime'][i] = pd.Timestamp(by_student_network_record_data['logintime'][i].year, by_student_network_record_data['logintime'][i].month, by_student_network_record_data['logintime'][i].day, 23,59,59)
#     if(i % 1000 == 0):
#         print(i)

# by_student_network_record_data.to_csv('by_student_network_record_data_handle.csv')


# 提取特征
# load data
by_student_network_record_data = pd.read_csv('by_student_network_record_data_handle.csv')
# 得到每个人每天的上网次数，按id，logintime排序
# by_student_network_record_data.groupby(['id','day'])['index'].count().reset_index().to_csv('network_count_by_day.csv')

# 提取一个新的表，为id，日，用于存放特征
# feature_network_id_day = by_student_network_record_data.groupby(['id', 'day']).sum().reset_index().iloc[:, [0, 1]]

# 找出每日平均total_mb的25%与75%
# temp = by_student_network_record_data.groupby(['id', 'day'])['total_mb'].sum().reset_index()

# temp.describe()

# temp['f_total_mb_by_day_75%'] = 0
# temp['f_total_mb_by_day_25%'] = 0

# temp['f_total_mb_by_day_75%'] = temp['total_mb'] > 609.271000
# temp['f_total_mb_by_day_25%'] = temp['total_mb'] < 50.569000

# temp['f_total_mb_by_day_75%'] = temp['f_total_mb_by_day_75%'].astype('int')
# temp['f_total_mb_by_day_25%'] = temp['f_total_mb_by_day_25%'].astype('int')

# feature_network_id_day['f_total_mb_by_day_75%'] = temp['f_total_mb_by_day_75%']
# feature_network_id_day['f_total_mb_by_day_25%'] = temp['f_total_mb_by_day_25%']

# feature_network_id_day.head()

# del temp
# gc.collect()

# # 找出每日平均duration_seconds的25%与75%
# temp = by_student_network_record_data.groupby(['id', 'day'])['duration_seconds'].sum().reset_index()

# temp.describe()

# temp['f_duration_seconds_by_day_75%'] = 0
# temp['f_duration_seconds_by_day_25%'] = 0

# temp['f_duration_seconds_by_day_75%'] = temp['duration_seconds'] > 6.756667
# temp['f_duration_seconds_by_day_25%'] = temp['duration_seconds'] < 1.633889

# temp['f_duration_seconds_by_day_75%'] = temp['f_duration_seconds_by_day_75%'].astype('int')
# temp['f_duration_seconds_by_day_25%'] = temp['f_duration_seconds_by_day_25%'].astype('int')

# feature_network_id_day['f_duration_seconds_by_day_75%'] = temp['f_duration_seconds_by_day_75%']
# feature_network_id_day['f_duration_seconds_by_day_25%'] = temp['f_duration_seconds_by_day_25%']

# feature_network_id_day.head()

# del temp
# gc.collect()

# # 找出每日平均duration_seconds的25%与75%
# temp = by_student_network_record_data.groupby(['id', 'day'])['in_mb'].sum().reset_index()

# temp.describe()

# temp['f_in_mb_by_day_75%'] = 0
# temp['f_in_mb_by_day_25%'] = 0

# temp['f_in_mb_by_day_75%'] = temp['in_mb'] > 478.084000
# temp['f_in_mb_by_day_25%'] = temp['in_mb'] < 41.442000

# temp['f_in_mb_by_day_75%'] = temp['f_in_mb_by_day_75%'].astype('int')
# temp['f_in_mb_by_day_25%'] = temp['f_in_mb_by_day_25%'].astype('int')

# feature_network_id_day['f_in_mb_by_day_75%'] = temp['f_in_mb_by_day_75%']
# feature_network_id_day['f_in_mb_by_day_25%'] = temp['f_in_mb_by_day_25%']

# feature_network_id_day.head()

# del temp
# gc.collect()

# # 找出每日平均duration_seconds的25%与75%
# temp = by_student_network_record_data.groupby(['id', 'day'])['out_mb'].sum().reset_index()

# temp.describe()

# temp['f_out_mb_by_day_75%'] = 0
# temp['f_out_mb_by_day_25%'] = 0

# temp['f_out_mb_by_day_75%'] = temp['out_mb'] > 57.763000
# temp['f_out_mb_by_day_25%'] = temp['out_mb'] < 4.951000

# temp['f_out_mb_by_day_75%'] = temp['f_out_mb_by_day_75%'].astype('int')
# temp['f_out_mb_by_day_25%'] = temp['f_out_mb_by_day_25%'].astype('int')

# feature_network_id_day['f_out_mb_by_day_75%'] = temp['f_out_mb_by_day_75%']
# feature_network_id_day['f_out_mb_by_day_25%'] = temp['f_out_mb_by_day_25%']

# feature_network_id_day.head()

# del temp
# gc.collect()

# # 找出第一次联网时间在7点到9点的
# by_student_network_record_data['hour'] = by_student_network_record_data['logintime'].dt.hour

# by_student_network_record_data['hour_7_9'] = (by_student_network_record_data['hour'] < 9) & ( 7<by_student_network_record_data['hour'])

# temp = by_student_network_record_data.groupby(['id', 'day'])['hour_7_9'].sum().reset_index()

# feature_network_id_day['f_first_record'] = (temp['hour_7_9'] >= 1)

# feature_network_id_day['f_first_record'] = feature_network_id_day['f_first_record'].astype('int')

# feature_network_id_day.to_csv('feature_network_id_day.csv')

feature_network_id_day = pd.read_csv('feature_network_id_day.csv')
print(feature_network_id_day.head())

# 统计每天的上网流量及时长
temp = by_student_network_record_data.groupby(['id','day'])['total_mb', 'duration_seconds'].sum().reset_index()

feature_network_id_day['total_mb_day'] = temp['total_mb']
feature_network_id_day['duration_seconds_day'] = temp['duration_seconds']

del temp
gc.collect()
# feature_network_id_day.to_csv('feature_network_id_day.csv')

