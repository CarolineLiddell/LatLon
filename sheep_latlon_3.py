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
import glob




filenames = glob.glob("C:/Phd/Alice/Bainbridge1/Bainbridge*.csv")

hFig = plt.figure("Sheep tracks")

for f in filenames:
    # remove spacing
    data = pd.read_csv(f)    
    data['Latitude'] = data[' Latitude']
    data['Longitude'] = data[' Longitude']
        
    # set start coordinates as those in row 0
    startlat = data.iloc[0].Latitude
    startlon = data.iloc[0].Longitude

    # create an empty array (number of rows, number of columns)
    # number of rows = len(data): as many rows as the dataframe "data" already has
    dis = np.empty((len(data), 1)) 
    head = np.empty((len(data), 1))
    start = LatLon.LatLon(startlat, startlon)
    for index in xrange(len(data)):
        
        # distance        
        walk = LatLon.LatLon(data.Latitude[index], data.Longitude[index])
        dis[index] = start.distance(walk)
        data['calc_distance'] = dis
        
        # heading        
        heading = LatLon.LatLon(data.Latitude[index], data.Longitude[index])
        head[index] = math.radians(90-start.heading_initial(heading))
        data['calc_heading'] = head
        
    # plot 
    x = dis * np.cos(head)
    y = dis * np.sin(head)
        
    plt.plot(x, y)
    
    #for index in xrange(len(data)):
   #     plt.plot(x[index],y[index])
   # plt.show()
    
    
# cutting off part of the route where sheep were on the road based on plot
#prex = dis * np.cos(head)
      
#ind = np.where(prex >= 3.120)
#index = ind[0][0]                       # row 1439

#cutdis = dis[index:]
#cutheading = head[index:]
#cutdata = data[index:]

#x = cutdis * np.cos(cutheading)
#y = cutdis * np.sin(cutheading)

    
