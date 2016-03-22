# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:19:52 2016

@author: cl516
"""

import numpy as np
import pandas as pd
import haversine
import matplotlib.pyplot as plt

# import data
data = pd.read_csv("C:/Phd/Alice/PyHM_Bainbridge1.csv", skipinitialspace=True)
sheep_summary = pd.read_csv("C:/Phd/Alice/Summary_Bainbridge.csv", delimiter = ',')
sheep_summary['Sheep_ID'] = sheep_summary['Sheep_ID '] # remove spacing

# convert hours and minutes to strings (length = 2 characters)
# need to be strings to create timestamp
data['Hours'] = data['Hours'].astype('S2')
data['Minutes'] = data['Minutes'].astype('S2')

# create a timestamp from the date, hours and minutes columns
data['timestamp'] = pd.to_datetime(data['Date'] + ' ' + data['Hours'] + ':' + data['Minutes'],
     format="%d/%m/%Y %H:%M")

# create empty lists to collect first and last GPS collar recordings of each sheep
start_last = []
end_first = []


# loop through all the sheep finding the maximum and minumum time stamp, add these to the lists
for sheepName in np.unique(data['Sheep_ID']):    
    min_t = (min(data['timestamp'][data['Sheep_ID']==sheepName]))     
    start_last.append(min_t)
    max_t = (max(data['timestamp'][data['Sheep_ID']==sheepName]))
    end_first.append(max_t)

# determine latest first GPS recording (start) and earliest last GPS recording (end)
start = max(start_last)
end = min(end_first)

# create new dataframe in which all sheep have same start and end time
data_cut = data.loc[(data.timestamp >= start) & (data.timestamp <= end)]

# group data according to timestamp, take mean latitude and longitude at each time
meanlat = data_cut.groupby(['timestamp'])['Latitude'].mean()
meanlon = data_cut.groupby(['timestamp'])['Longitude'].mean()


def getColumnDataForSheep(sheepID, colName, dataFrame):
   return dataFrame.loc[data_cut['Sheep_ID'] == sheepID, colName]

# get array of all the sheep names
sheeps = np.unique(data_cut.loc[:, 'Sheep_ID'])

# create dictionaries
distance_centre = {}
FEC = {}

# get latitude and longitude for each sheep at every timestep
for sheep in sheeps:
    lat = getColumnDataForSheep(sheep, 'Latitude', data_cut).tolist()
    lon = getColumnDataForSheep(sheep, 'Longitude', data_cut).tolist()
 
    # create a list
    current_sheeps_distance = []
    for i in range(0, len(lat)):
        current_coord = lat[i], lon[i]      # combine lat and lon at each time step into coordinate
        centre = meanlat[i], meanlon[i]     # combine mean lat and lon of all sheep into coordinate
        distance = haversine.haversine(centre, current_coord) * 1000    # calcluate distance of individual sheep to centre of the group (*1000 for meters)
        current_sheeps_distance.append(distance)                        # append distance to list
    distance_centre[sheep] = np.mean(current_sheeps_distance)           # calculate mean distance and append to dictionary
                                                                        # with [sheep] = sheepname as key and distance as value
    # collect FEC values and store them in a dictionary
    FEC[sheep] = sheep_summary.loc[sheep_summary['Sheep_ID']==sheep].FEC.values[0]


# plot mean distance from centre of group again faecal egg count
plt.xlabel("average distance from centre")
plt.ylabel("FEC") 
plt.scatter(distance_centre.values(), FEC.values())