#!/usr/bin/env python
# coding: utf-8

# Exercise 1. 
# - You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

# In[1]:


The_little_mermaid = 3


# In[2]:


Brother_Bear = 5


# In[3]:


Hercules = 1


# In[4]:


Movies_rented = [The_little_mermaid, Brother_Bear, Hercules]


# In[5]:


Price_paid = [i * 3 for i in Movies_rented]


# In[6]:


Price_paid


# In[12]:


sum(Price_paid)


# In[26]:


# I will have to pay $27


# Exercise 2. 
# - Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

# In[7]:


Google = 400


# In[8]:


Amazon = 380


# In[9]:


Facebook = 350


# In[10]:


Money_per_hour_per_company = [Google, Amazon, Facebook]


# In[11]:


Money_per_hour_per_company


# In[13]:


Google_dollars = Google * 6


# In[14]:


Google_dollars


# In[15]:


Amazon_dollars = Amazon * 4


# In[17]:


Amazon_dollars


# In[18]:


Facebook_dollars = Facebook * 10 


# In[19]:


Facebook_dollars


# In[23]:


This_Week_in_dollars = Google_dollars + Amazon_dollars + Facebook_dollars


# In[24]:


This_Week_in_dollars


# In[25]:


# This week I made $7420


# Exercise 3. 
# - A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

# In[38]:


is_there_room = True


# In[39]:


are_there_conflicts = False


# In[40]:


can_she_enroll = is_there_room and not are_there_conflicts


# In[41]:


can_she_enroll


# Exercise 4. 
# - A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

# In[49]:


more_than_two = True


# In[54]:


expired = False


# In[51]:


premium_member = False


# In[55]:


Product_offer = (more_than_two and not expired) or premium_member

Product_offer
# Exercise 5. 
# - Use the following code to follow the instructions below:
#     - username = 'codeup'
#     - password = 'notastrongpassword'
# - Create a variable that holds a boolean value for each of the following conditions:
# 
#     - the password must be at least 5 characters
#     - the username must be no more than 20 characters
#     - the password must not be the same as the username
#     - bonus neither the username or password can start or end with whitespace
# 
# 

# In[3]:


username = 'codeup'


# In[4]:


password = 'notastrongpassword'


# In[5]:



at_least_5 = len(password)>=5


# In[6]:


at_least_5


# In[7]:


twenty_only = len(username)<=20


# In[8]:


twenty_only


# In[12]:


unique_credentials = password != username


# In[13]:


unique_credentials


# In[21]:


leading_whitespace_password = password[0] in ' '


# In[22]:


trailing_whitespace_password = password[-1] in ' '


# In[23]:


leading_whitespace_username = username[0] in ' '


# In[24]:


trailing_whitespace_username = username[-1] in ' '


# In[25]:


leading_whitespace_password


# In[26]:


trailing_whitespace_password


# In[27]:


leading_whitespace_username


# In[28]:


trailing_whitespace_username


# In[ ]:




