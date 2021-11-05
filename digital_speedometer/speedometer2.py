from math import pi
import numpy as np
from time import sleep
def velocity(t,r = 0.3):
    rps = 1/t                     #t : time taken for one revolution
    circumference = 2*pi*r        #r : radius of the wheel
    v = rps*circumference         # gives the velocity in m/s
    return np.round(v*3.6,2)      # returns velocity in km/hr
def distance(rev,r = 0.3):
    return rev*2*pi*r
rf = lambda x:x**2-2*x+1.06  #function to give time taken for one revolution
tot_dist = 0
time = 0
for i in np.linspace(0,2,10):   
    t = rf(i)
    time+=t
    sleep(t)
    tot_dist+=distance(1)
    print(f'Speed = {velocity(t)} km/hr  Distance = {np.round(tot_dist,2)} m  time = {round(time,2)} s   \r',end = "")
