#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# In[2]:


# BMI is weight in kilograms divided by height in meters squared.
# BMI = Weight in kilograms / height in meters squared.


# In[17]:


Weight = input("Enter your weight in Kilograms: ")

Height = input("Enter your weight in Centimeter: ")

Height = int(Height)
Weight = int(Weight)

Height = Height / 100

Height_Square = Height*Height

BMI = Weight / Height_Square

print(BMI)


# In[ ]:




