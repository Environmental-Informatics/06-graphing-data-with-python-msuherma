# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 17:33:46 2020

@author: Mukhamad Suhermanto
HW6:
    This program is used to manage text files and generates plot of the data.
    The text files
"""
# one of the source I used to learn: https://www.youtube.com/watch?v=n-WGUz3ZkBY
# Initially I get this message while trying to load using numpy loadtxt : "could not convert string to float: 'Year' "

# Importing used packages in this 
import numpy as np
import matplotlib.pyplot as plt

#I began to the project by reading the data first using following, to understand clearly about the instruction

#[3] Setting to fulfill the 3 point, i.e. enabling changing input for processing
d = open("Tippecanoe_River_at_Ora.Annual_Metrics.txt") 
'''
text = d.read() 
d.close()
print(text)
'''
#Change the file here

#[1] using Numpy genfromtxt() to load provided data "Wildcat_Creek_at_Lafayette.Annual_Metrics.txt"
d=np.genfromtxt('Wildcat_Creek_at_Lafayette.Annual_Metrics.txt', names=True)
#Plotting process

#[2] Single page to draw three plots using subplot (Reference: https://www.youtube.com/watch?v=XFZRVnP-MTU)
plt.style.use('seaborn')

#setting for 3 plots in 1 page. p1,p2,p3 are top, middle, and bottom plots respectively

fig, (p1, p2, p3) = plt.subplots(nrows = 3, ncols = 1)

# x =axis is the year, 
# since 'Year' is always the x-axis, it is better to simplify here
x=d['Year']

#[2.1] Top Plot, with the mean (black), maximum (blue) and minimum (blue)
#in matplotlib, black is 'k', blue

#p1. 

p1.plot(x,d['Mean'],'k',x,d['Max'],'r',x,d['Min'],'b') 
p1.set_xlabel('Year') 
p1.set_ylabel('Streamflow')
p1.legend(['Mean','Maximum','Minimum'],prop={'size':6})

#[2.2] Mid Plot, The annual value of Tqmean multiplied by 100
#p2 
p2.plot(x,d['Tqmean']*100,'g^') 
p2.set_xlabel('Year') 
p2.set_ylabel('Tq_mean (%)')

#[2.3] Bottom Plot, Bar plot of R-B index

#p3.plot(313) 
p3.bar(x,d['RBindex']) 
p3.set_xlabel('Year') 
p3.set_ylabel('R-B Index')

plt.tight_layout()
plt.savefig('Wildcat_Creek.pdf')
