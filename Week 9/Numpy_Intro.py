#Name: Brendan Gee
#Date: 5/29/21
#Video Link: https://youtu.be/yoNJ529xEDw
#Honor Statement: I have not given or received any unauthorized assistance on this assignment

import numpy as np
import random

a = np.arange(0,100)
b = np.arange(0,100,10) #spacing 10
c = np.linspace(0,10,101) #101 since it is including 10
d = np.linspace(0, random.randrange(1,11), 100).reshape(10,10) #selects a rand int 1-10 and spaces out 100 times
a = a.reshape(10,10) #reshapes a to 2-D 10x10
print(a[4,5])
print(a[4])
print(np.sum(d))
print(np.max(a))
print(np.transpose(b))
print(a + d)
print(a * d) #multiplies through by i,j character in a,d
print(np.dot(a,d)) #takes the sum of products
