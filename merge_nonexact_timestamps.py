import pandas as pd
from pandas import read_csv
from io import StringIO

# datetime column (combination of date + start_time)
dtc = [['date', 'start_time']]

# index column (above combination)
ixc = 'date_start_time'

df1 = read_csv(StringIO(u'''
date,start_time,employee_id,session_id
01/01/2016,02:03:00,7261824,871631182
01/01/2016,06:03:00,7261824,871631183
01/01/2016,11:01:00,7261824,871631184
01/01/2016,14:01:00,7261824,871631185
'''), parse_dates=dtc)

df2 = read_csv(StringIO(u'''
date,start_time,employee_id,session_id
01/01/2016,02:03:00,7261824,871631182
01/01/2016,06:05:00,7261824,871631183
01/01/2016,11:04:00,7261824,871631184
01/01/2016,14:10:00,7261824,871631185
'''), parse_dates=dtc)



df1['date_start_time'] = pd.to_datetime(df1['date_start_time'])
df2['date_start_time'] = pd.to_datetime(df2['date_start_time'])

# converting this to the index so we can preserve the date_start_time columns so you can validate the merging logic
df1.index = df1['date_start_time']
df2.index = df2['date_start_time']
# the magic happens below, check the direction and tolerance arguments
tol = pd.Timedelta('5 minute')
res = pd.merge_asof(left=df1,right=df2,right_index=True,left_index=True,direction='nearest',tolerance=tol)

print(res)