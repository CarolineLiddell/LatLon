import numpy as np
import pandas as pd
import os, re
import math
import time

import matplotlib.pyplot as plt
import matplotlib.animation as ani

HD = os.getenv('HOME')







posfilename =HD +  '/Dropbox/Sheep_Files_1/PyHM_Kate1.csv'
posDF = pd.read_csv(posfilename) 
posDF['x'] = posDF['calc_distance'].values*np.cos(posDF['calc_heading'])
posDF['y'] = posDF['calc_distance'].values*np.sin(posDF['calc_heading'])
        
fig = plt.figure(figsize=(10, 10), dpi=100)
for fnum, frame in posDF.groupby(['Hours','Minutes']):
    break
    xp = frame['x'].values
    yp =  frame['y'].values
    plt.clf()
    plt.plot(xp, yp,'k.')
    plt.axes().set_aspect('equal')
    plt.axis([-0.5,0.5,-0.5,0.5])
    plt.draw()
#    plt.savefig('figs/fig'+str(fnum)+'png')
    time.sleep(0.01)




fig = plt.figure(figsize=(10, 10), dpi=100)
l, = plt.plot([], [], 'ro')
plt.axis([-0.25,0.25,-0.25,0.25])

seconds = 30
totalFrames = 10*seconds
fc = 0
FFMpegWriter = ani.writers['ffmpeg']
metadata = dict(title='animation of movement')
writer = FFMpegWriter(fps=10, metadata=metadata)

#    
with writer.saving(fig, "move.mp4", totalFrames):# len(posDF.groupby('frame'))):


    for fnum, frame in posDF.groupby(['Hours','Minutes']):
        #break
        fc = fc + 1
        if fc>totalFrames:
            break
        xp = frame['x'].values
        yp =  frame['y'].values
        l.set_data(xp, yp)
        writer.grab_frame()

