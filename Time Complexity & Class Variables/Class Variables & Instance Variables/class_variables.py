#!/usr/bin/env python
# coding: utf-8

# ## Class variables
# * Class variables are shared by all instances
# * Instance variables are unique to each instance

# In[32]:


class CarDetails:
    rating = []           #class variable 
    def __init__(self,name):
        self.name = name  #instance variable
        
    def add_rating(self,rating):
        self.rating.append(rating)


# In[27]:


car1 = CarDetails('audi')
car1.name


# In[28]:


car2 = CarDetails('benz')
car2.name


# In[29]:


print(car1.rating, car2.rating)


# In[30]:


car2.add_rating(9)
car2.rating


# In[33]:


car1.rating              #rating is shared to car1


# In[3]:


class CarDetails:
    def __init__(self,name):
        self.name = name
        self.rating = []
        
    def add_rating(self,rating):
        self.rating.append(rating)


# In[4]:


car1 = CarDetails('audi')
car2 = CarDetails('benz')
car2.add_rating(5)
print(car1.rating,car2.rating)

