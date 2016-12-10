import numpy as np
import pandas as pd
import os
import math

file_=r'/home/zsolt/DATA/msc_100k.csv'
msck = pd.read_csv(file_, sep = ',', names = ["TAC","Type","timestamp","unix","latitude","longitude"])

print(msck.head())

def isInBudapest(lati,longi):
	#bafelso
	ax = 47.517559 
	ay = 19.052176
	
	#jobbalso
	dx = 47.478452
	dy = 19.106307

	inX = False
	inY = False

	if(lati > dx and lati < ax):
		inX = True
	if(longi > dy and longi < ay):	
		inY = True

	return (inX and inY)


# print(isInBudapest(47.499620, 19.058110))

for index,row in msck.iterrows():
	lati = row['latitude']
	longi = row['longitude']
	content = 'new google.maps.LatLng(' + str(lati) + ',' + str(longi) + '),'
	
	if (content != 'new google.maps.LatLng(nan,nan),'):
		if (isInBudapest(lati,longi)):
			with open('./output.txt', 'a') as f1:
				f1.write(content + os.linesep)


