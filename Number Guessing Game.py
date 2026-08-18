#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
n = random.randint(1,100)

guess = 0
while True:
    a = int(input("Enter a number Between 1 to 100 : "))
    guess += 1

    if a>100 :
        print("Dont enter more than 100")

    elif(a>n):
        print("Lower number Please ! ")

    elif(a<n):
        print("Higher number Please ! ")

    else :
        print(f"You have guesse the number {n} correctly in {guess} attempts")
        break



# In[ ]:




