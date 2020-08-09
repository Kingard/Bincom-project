#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1.      Which color of shirt is the mean color?
# 2.      Which color is mostly worn throughout the week?
# 3.      Which color is the median?
# 4.      BONUS Get the variance of the colors
# 5.      BONUS if a colour is chosen at random, what is the probability that the color is red?
# 6.      Save the colours and their frequencies in postgresql database
# 7.      BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.
# 8.      Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
# 9.      Write a program to sum the first 50 fibonacci sequence.


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


x = pd.read_html('python_class_question.html')


# In[4]:


x_table = pd.DataFrame(x[0])


# In[5]:


x_table


# In[6]:


colours = []
for i in range(len(x_table['DAY'])):
    print(x_table['COLOURS'][i])
    colours.append(x_table['COLOURS'][i])
    
        
#colours
#len(x_table['DAY'])


# In[7]:


mid_week_colours = colours[(len(colours)-1)//2]
median_colour = list(mid_week_colours[(len(mid_week_colours)-1)//2])
median_colour = mid_week_colours.split(',')[(len(mid_week_colours.split(','))-1)//2]


# In[8]:


median_colour


# In[91]:


# 9. FIBONACCI
range_ = 50
lxt = [0,1]
for n in range(1,range_-1):
    next_num = lxt[-1]+lxt[n-1]
    n+=1
        
    lxt.append(next_num)
        
print(lxt)


# In[98]:


colours[:]


# In[126]:


# 2. MOST WORN COLOUR IS BLUE, # 1. Mean colour is BLUE
import collections
#collections.Counter(x_table['COLOURS'][0])
for i in range(5):
    x = collections.Counter(x_table['COLOURS'][i].split(','))
    print(x)


# In[19]:


# 8. Generate random binary numbers and convert to base 10

# Python program for random 
# binary string generation 
  
import random 
import math
  
# Function to create the 
# random binary string 
def rand_key(p): 
    
    # Variable to store the  
    # string 
    key1 = "" 
  
    # Loop to find the string 
    # of desired length 
    for i in range(p): 
          
        # randint function to generate 
        # 0, 1 randomly and converting  
        # the result into str 
        temp = str(random.randint(0, 1)) 
  
        # Concatenatin the random 0, 1 
        # to the final result 
        key1 += temp 
          
    return(key1) 
  
# Driver Code 
p = 4
b = rand_key(p) 
print(" The binary number is : ", b) 


def bin2dec(b):
    number = 0
    for idx, num in enumerate(b[::-1]): # Iterating through b in reverse order
        number += int(num)*(2**idx)

    return number


# In[20]:




def bin2dec(b):
    number = 0
    for idx, num in enumerate(b[::-1]): # Iterating through b in reverse order
        number += int(num)*(2**idx)

    return number


# In[21]:


bin2dec(b)


# In[ ]:




