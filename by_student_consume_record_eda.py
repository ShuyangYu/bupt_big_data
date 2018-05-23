# coding: utf-8

import gc
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import gridspec

pd.set_option('max_colwidth', 200)

by_student_consume_record_data = pd.read_csv(
    'consume_info_data.csv')

by_student_consume_record_data = by_student_consume_record_data.dropna(axis=0)

by_student_consume_record_data['datetime'] = pd.to_datetime(
    by_student_consume_record_data['datetime'])

## Someone

# someone_data = by_student_consume_record_data[by_student_consume_record_data['id'] == '7e397ee2361de4efe633aa82fe39ff5a']

# temp = someone_data.day.str.split(pat='-', expand=True)

# someone_data['year_month'] = temp[0] + '-' + temp[1]

# groupby_year_month_type = someone_data.groupby(['year_month', 'type'])['remainder'].sum().reset_index().sort_values(by='year_month')

# groupby_year_month = someone_data.groupby(['year_month'])['remainder'].sum().reset_index().sort_values(by='year_month')

# # 分类绘图someone
# fig, ax = plt.subplots(figsize = (25,5))
# sns.barplot(x = "year_month", y  = "remainder", hue='type', data = groupby_year_month_type, ax = ax)

# # 分类绘图someone
# fig, ax = plt.subplots(figsize = (25,5))
# sns.barplot(x = "year_month", y  = "remainder", data = groupby_year_month, ax = ax)

# # ### 洗澡时间
# someone_shower_data = someone_data[someone_data['type'] == '淋浴支出']

# del_rows = []
# for i in range(someone_shower_data.shape[0]-1):
#     if((someone_shower_data.iloc[i + 1]['datetime'] - someone_shower_data.iloc[i]['datetime']) <  pd.to_timedelta('0 days 2:00:00')):
#         del_rows.append(i+1)

# new = someone_shower_data.drop(del_rows)

# new['time_to_seconds'] = pd.to_timedelta(new['time']).dt.total_seconds()

# new['hour'] = new['datetime'].dt.hour

# new = new[new['hour'] > 11]
# new = new[new['hour'] < 23]

# fig, ax = plt.subplots(figsize = (25,5))
# sns.pointplot(x="day", y="time_to_seconds", data=new,
# #               palette={"male": "g", "female": "m"},
#                 markers=["^", "o"], linestyles=["-", "--"])

# sns.swarmplot(x='type', y='time_to_seconds', data=new)

# # ### 吃饭时间
# someone_chi_data = someone_data[someone_data['type'] == '餐费支出']

# someone_chi_data['total_seconds'] = pd.to_timedelta(someone_chi_data['time']).dt.total_seconds()

# someone_chi_data['hour'] = someone_chi_data['time'].str.split(pat=':',expand=True)[0]

# someone_chi_data['hour'] = someone_chi_data['hour'].astype('int')

# sns.distplot(someone_chi_data['hour'])
# ## 整体
consume_record_data_sort = by_student_consume_record_data.sort_values(
    by=['id', 'datetime'])

if os.path.exists('consume_record_data_sort_shower.csv'):
    print('consume_record_data_sort_shower.csv    exist')
    print('loading...')

    consume_record_data_sort_shower = pd.read_csv('consume_record_data_sort_shower.csv')
else:
    print('consume_record_data_sort_shower.csv    missing')
    print('handle...')

    consume_record_data_sort_shower = consume_record_data_sort[
        consume_record_data_sort['type'] == '淋浴支出'].reset_index()

    del_rows = []
    for i in range(consume_record_data_sort_shower.shape[0] - 1):
        if ((consume_record_data_sort_shower.iloc[i + 1]['datetime'] -
             consume_record_data_sort_shower.iloc[i]['datetime']) <
                pd.to_timedelta('0 days 2:00:00')):
            del_rows.append(i + 1)
        if (i % 100000 == 0):
            print(i)

    consume_record_data_sort_shower = consume_record_data_sort_shower.drop(
        del_rows)

    consume_record_data_sort_shower.to_csv(
        'consume_record_data_sort_shower.csv')

# # 存储吃饭数据
# by_student_consume_record_data_sort_by_id_datetime_chi = consume_record_data_sort[
#     consume_record_data_sort['type'] == '餐费支出'].reset_index()

# by_student_consume_record_data_sort_by_id_datetime_chi.to_csv(
#     'by_student_consume_record_data_sort_by_id_datetime_chi.csv')
# # 处理商场购物
# by_student_consume_record_data_sort_by_id_datetime_shopping = consume_record_data_sort[
#     consume_record_data_sort['type'] == '商场购物'].reset_index()

# by_student_consume_record_data_sort_by_id_datetime_shopping.to_csv(
#     'by_student_consume_record_data_sort_by_id_datetime_shoopping.csv')

# consume_record_data_sort_shower['total_seconds'] = pd.to_timedelta(
#     consume_record_data_sort_shower['time']).dt.total_seconds()

# consume_record_data_sort_shower['weekday'] = consume_record_data_sort_shower[
#     'datetime'].dt.weekday

# consume_record_data_sort_shower['hour'] = consume_record_data_sort_shower[
#     'datetime'].dt.hour

# consume_record_data_sort_shower = consume_record_data_sort_shower[
#     consume_record_data_sort_shower['hour'] > 11]
# consume_record_data_sort_shower = consume_record_data_sort_shower[
#     consume_record_data_sort_shower['hour'] < 23]

# consume_record_data_sort_shower.groupby(['weekday',
#                                          'hour']).count().reset_index().head()
