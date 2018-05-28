# coding: utf-8

import gc
import os

import numpy as np
import pandas as pd

network_record_day_mb_time = pd.read_csv('network_record_day_mb_time.csv')
network_record_day_class = pd.read_csv('network_record_day_class.csv')
feature_network_id_day = pd.read_csv('feature_network_id_day.csv')
network_count_by_day = pd.read_csv('network_count_by_day.csv')
night_network_time = pd.read_csv('night_network_time.csv')

consume_record_day_meal_fee = pd.read_csv('consume_record_day_meal_fee.csv')
print(consume_record_day_meal_fee.shape)

feature_id_day = pd.read_csv('feature_id_day.csv')

print(network_count_by_day.shape, feature_id_day.shape)

temp = pd.merge(
    network_record_day_mb_time,
    network_record_day_class,
    on=['id', 'day'],
    how="outer")
temp = pd.merge(temp, feature_network_id_day, on=['id', 'day'], how="outer")
temp = temp.drop(
    labels=['Unnamed: 0_x', 'Unnamed: 0', 'Unnamed: 0_y', 'Unnamed: 0'],
    axis=1)

# merge 每日上网次数
feature_id_day = pd.merge(
    feature_id_day, network_count_by_day, on=['id', 'day'], how="outer")

# merge 晚自习上网时长
feature_id_day = pd.merge(
    feature_id_day, night_network_time, on=['id', 'day'], how="outer")

feature_id_day.to_csv('feature_id_day.csv')
