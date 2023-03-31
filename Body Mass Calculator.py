#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# In[2]:


# BMI is weight in kilograms divided by height in meters squared.
# BMI = Weight in kilograms / height in meters squared.


# In[34]:


Weight = input("Enter your weight in Kilograms: ")

Height = input("Enter your weight in Centimeter: ")

Height = int(Height)
Weight = int(Weight)

Height = Height / 100

Height_Square = Height*Height

BMI = Weight / Height_Square

print(BMI)

if BMI <  18.5:
    print("You are Underweigth")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are Normal Weight")
elif BMI >= 25 and BMI <=29.9:
    print("You are Over weight")
else:
    print("You are Obese")

