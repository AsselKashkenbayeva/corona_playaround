import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Upload_data:

	def __init__(self, input_path):
		self.file = pd.read_csv(abs_path)
		print ('Download complete!')
		
abs_path = "/Users/assel2/python_dir/corona_play/coronavirusdataset/patient.csv"
corona_data = Upload_data(abs_path)

corona_data = pd.DataFrame(corona_data.file)

print('There are %d number of rows in this data set' %len(corona_data))
print('This data set contains',list(corona_data),' details')

print('Within the dataset, there is %d overall deseased patients' %sum(corona_data['deceased_date'].value_counts()))
total_deceased = (sum(corona_data['deceased_date'].value_counts()/(len(corona_data)/100)))
print('That means that the overall death rate is:', total_deceased,'%')

deceased_num = corona_data['deceased_date'].value_counts()
print(deceased_num)
#deceased_num.plot()
#plt.show()
from datetime import date
conf_dates = pd.to_datetime(corona_data['confirmed_date'])
print(conf_dates.head(3))
release_dates = pd.to_datetime(corona_data['released_date'])
#print(release_dates.head(3))

recovery_time = conf_dates - release_dates
#print(recovery_time)
days_to_recovery = recovery_time.value_counts().sort_index()
#print(days_to_recovery)
#days_to_recovery.plot()
#plt.show()

new_df = pd.Series([recovery_time], name = 'recovery_time')
new_df.to_frame()
print(len(new_df))