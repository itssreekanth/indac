from math import pi
import numpy as np
from time import sleep
def velocity(t,r = 0.1):
    rps = 1/t                     #t : time taken for one revolution
    circumference = 2*pi*r        #r : distance of sensor from the centre of wheel
    v = rps*circumference         # gives the velocity in m/s
    return np.round(v*3.6,2)      # returns velocity in km/hr
def distance(rev,r = 0.3):        #r : radius of the wheel
    return rev*2*pi*r             
s = np.random.rand(10)            #randomly picks time values for n revolutions
tot_dist = 0
time = 0
for i in s:
    sleep(i)          
    time+=i
    tot_dist+=distance(1)
    print(f'Speed = {velocity(i)} km/hr  Distance = {np.round(tot_dist,2)} m  time = {round(time,2)} s  \r',end = "")
