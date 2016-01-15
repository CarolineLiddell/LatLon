# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 11:23:00 2015

@author: cl516
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 13:58:02 2015

@author: cl516
"""
import os
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import LatLon

data = pd.read_csv("C:/Phd/Alice/Amos1/Amos103.csv")

os.chdir("C:/Phd/Alice/Amos1/")


files = os.listdir(os.getcwd())
sheep = np.empty((len(files), 1)) 
for index in xrange(len(files)):
    distance()
    
    

# remove spacing
    data['Latitude'] = data[' Latitude']
    data['Longitude'] = data[' Longitude']

        
# set start coordinates as those in row 0
    startlat = data.iloc[0].Latitude
    startlon = data.iloc[0].Longitude

# create an empty array (number of rows, number of columns)
# number of rows = len(data): as many rows as the dataframe "data" already has
dis = np.empty((len(data), 1)) 
def distance():    
    for index in xrange(len(data)):
        start = LatLon.LatLon(startlat, startlon)
        walk = LatLon.LatLon(data.Latitude[index], data.Longitude[index])
        dis[index] = start.distance(walk)
       
    data['calc_distance'] = dis

head = np.empty((len(data), 1))
def heading():
    for index in xrange(len(data)):
        start = LatLon.LatLon(startlat, startlon)
        head = LatLon.LatLon(data.Latitude[index], data.Longitude[index])
        head[index] = math.radians(90-start.head_initial(head))

    data['calc_heading'] = head

# cutting off part of the route where sheep were on the road based on plot
    prex = dis * np.cos(heading)
      
    ind = np.where(prex >= 3.120)
    index = ind[0][0]                       # row 1439

    cutdis = dis[index:]
    cutheading = heading[index:]
    cutdata = data[index:]

    x = cutdis * np.cos(cutheading)
    y = cutdis * np.sin(cutheading)

    plt.plot(x,y)
    plt.show()
