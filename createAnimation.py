import numpy as np
import pandas as pd
import os, re
import math
import time

import matplotlib.pyplot as plt
import matplotlib.animation as ani

HD = os.getenv('HOME')




FFMpegWriter = ani.writers['ffmpeg']
metadata = dict(title='animation of movement')
writer = FFMpegWriter(fps=10, metadata=metadata)


posfilename = 'path/to/csv/file.csv'
posDF = pd.read_csv(posfilename) 
        
fig = plt.figure(figsize=(10, 10), dpi=100)

l, = plt.plot([], [], 'ro')
plt.axis([0,4000, 2000,-2000])



seconds = 30
totalFrames = 10*seconds
fc = 0
with writer.saving(fig, "move.mp4", totalFrames):# len(posDF.groupby('frame'))):


    for fnum, frame in posDF.groupby('frame'):
        fc = fc + 1
        if fc>totalFrames:
            break
        xp = frame['x'].values
        yp =  frame['y'].values
        l.set_data(xp, yp)
        writer.grab_frame()

