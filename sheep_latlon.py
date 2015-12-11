# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 13:58:02 2015

@author: cl516
"""
import numpy as np
import pandas as pd
data = pd.read_csv("C:/Phd/Alice/Amos1/Amos103.csv")

# set start coordinates as those in row 0
startlat = data.iloc[0].Latitude
startlon = data.iloc[0].Longitude

# remove spacing
data['Latitude'] = data[' Latitude']
data['Longitude'] = data[' Longitude']

import LatLon

# dis2 = np.empty((len(data), 1)) 
# for index, row in data.iterrows():
#    start = LatLon.LatLon(startlat, startlon)
#    walk = LatLon.LatLon(row.Latitude, row.Longitude)
#    dis2[index] = start.distance(walk)

# create an empty array (number of rows, number of columns)
# number of rows = len(data): as many rows as the dataframe "data" already has
dis = np.empty((len(data), 1))   
for index in xrange(len(data)):
    start = LatLon.LatLon(startlat, startlon)
    walk = LatLon.LatLon(data.Latitude[index], data.Longitude[index])
    dis[index] = start.distance(walk)

data['calc_distance'] = dis

heading = np.empty((len(data), 1))
for index in xrange(len(data)):
    start = LatLon.LatLon(startlat, startlon)
    head = LatLon.LatLon(data.Latitude[index], data.Longitude[index])
    heading[index] = start.heading_initial(head)

data['calc_heading'] = heading
    