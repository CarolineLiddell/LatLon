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

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import LatLon
import glob
import os


filenames = glob.glob("C:/Phd/Alice/Btest/Bainbridge*.csv")
sheep = pd.read_csv("C:/Phd/Alice/Summary_Btest.csv", delimiter = ',')
sheep['total_distance']=0

#filenames = glob.glob("C:/Phd/Alice/Bainbridge1/Bainbridge*.csv")
#sheep = pd.read_csv("C:/Phd/Alice/Summary_Bainbridge.csv", delimiter = ',')

#filenames = glob.glob("C:/Phd/Alice/Kate1/Kate*.csv")
#sheep = pd.read_csv("C:/Phd/Alice/Summary_Kate.csv", delimiter = ',')

#filenames = glob.glob("C:/Phd/Alice/Redlands1/Redlands*.csv")
#sheep = pd.read_csv("C:/Phd/Alice/Summary_Redlands.csv", delimiter = ',')

# create a new column in the summary file for distance


## CALCULATE DISTANCE AND HEADING FROM GPS TRACKS  


for f in filenames:
    # extract the extension (.csv) from a filename, so that sheepname can equal filename    
    sheepname = os.path.basename(f) # returns the base (end) of the path
    sheepname = sheepname[0:-4] # removes the last 4 characters (".csv") from name
    FEC = sheep.loc[sheep['Sheep_ID ']==sheepname].FEC.values[0]
    print("Processing %s" % sheepname)    
    
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
        
    
    
    # plot a scatter graph for distance vs FEC
    plt.scatter(sum(dis), FEC)
    plt.xlabel("distance")
    plt.ylabel("FEC")
    
    #sheep[sheep[['Sheep_ID ']]==sheepname]
    sheep[sheep[['Sheep_ID ']]==sheepname]['total_distance'] = float(sum(data['calc_distance']))
    sheep.loc[sheep[['Sheep_ID ']]==sheepname, ['total_distance']] = float(sum(data['calc_distance']))
   
   # plot 
   # x = dis * np.cos(head)
   # y = dis * np.sin(head)
    
   # if FEC <= 100:    
   #     plt.plot(x, y, color = 'g')
   # elif FEC > 100 and FEC <= 400:
   #     plt.plot(x, y, color = 'y')
   # else:
   #     plt.plot(x, y, color = 'r')

    # plot distance vs FEC

       
       


    

    
