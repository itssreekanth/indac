#!/usr/bin/env python
# coding: utf-8

# # Time Complexity & Big 'O' notation

# * If we take a algorithm or a function, how much time they take to complete the program
# * But execution speed is dependent on many factors, like cpu, os, and cpu load
# * So looking at execution time of programm is not a best way to calculate time complexity
# * It is wise to ask how does the runtime of the function grow with respect to size of input
# * Time complexity is represented by big 'O' notation

# ### Big 'O' notation :
# * It is the easy way to represent time complexity by big 'O' notation
# * example : O(g(x)) where g(x) describes the behaviour of runtime as input size increases
# * There are different type of function as given below

# ### Constant time  O(1) :
# * Execution time doesn't increase with respect to size of input

# In[2]:


# import required modules
import matplotlib.pyplot as plt
import numpy as np
import time


# checks time complexity of given function and plot a graph
def check_time_complexity(func):
    count = 1                         #size of the input
    xpoints = []
    ypoints = []
    
    while count <= 20**2:            #increases input value by 5 upto 400
        array = list(range(count))   #creates an list a natural numbers upto given input
        
        start = time.time()
        get_values = func(array)     
        end = time.time()
        
        time_elapsed = end-start     #calculates execution time of given function only
        
        xpoints.append(count)
        ypoints.append(time_elapsed)
        
        count += 5
    
    plt.plot(xpoints, ypoints, marker = 'o')
    plt.xlabel("size of input")     # xaxis is size of input
    plt.ylabel("time taken")        # yaxis is execution time
    plt.show()                      


def empty_func(array):
    total = 0
    return total


check_time_complexity(empty_func)


# ### Linear time O(n) :

def get_sum(array):
    total = 0
    
    for num in array:
        total += num
        
    return total


check_time_complexity(get_sum)


# ### Quadratic time O(n^2):


def get_product(array):
    total = 0
    
    for num1 in array:
        for num2 in array:
            total += num1*num2
    return total


check_time_complexity(get_product)

def get_sum(array):     #time taken = c1
    total = 0           #c2
    
    for num in array:   #c3 * (n+1)
        total += num    #c4 * n
        
    return total        #c5

c1 + c2 + c5 + c3*(n+1) + c4*n
C1 + n*c3 + c3 + n*c4
C2 + n(c3+c4)
C2 + n*C3  ==> O(n) linear time
# * **Time Complexity tell's us growth of run time as the size of input increases**
