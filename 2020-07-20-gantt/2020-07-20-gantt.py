#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 00:10:33 2020

@author: sheldon
"""

import pandas as pd
import datetime
import plotly.figure_factory as ff
from plotly.offline import plot
df=pd.read_csv("/home/sheldon/Documents/bicycle_data/06.csv")


df['Start']=df['started_at']
df['Finish']=df['ended_at']
df['Task']=df['end_station_name']

id_of_station_to_analyze=503
name_of_station_to_analyze=df[df['start_station_id']==id_of_station_to_analyze]['start_station_name'][0]

day_to_analyze=datetime.date(2020,6,3)
start_time=day_to_analyze.strftime("%Y-%m-%d")+" 00:00:00"
end_time=day_to_analyze.strftime("%Y-%m-%d")+" 23:59:59"


df=df[df['start_station_id']==id_of_station_to_analyze]
df=df[df['started_at'].between(start_time,end_time)]
df=df.reset_index()

title="From "+name_of_station_to_analyze+" to..."

fig1 = ff.create_gantt(df, title=title, group_tasks=True, height=1000)

plot(fig1)

