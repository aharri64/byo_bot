#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time, requests

from keys import path


# In[2]:


driver = webdriver.Chrome('/Users/amirharrison/downloads/chromedriver')


# In[3]:


driver.get('https://www.glassdoor.com/')


# In[4]:


driver.find_element_by_xpath('//*[@id="TopNav"]/nav/div/div/div[4]/div[1]/a').click()


# In[ ]:


driver.find_element_by_xpath('//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[1]/div/label').send_keys(username)
driver.find_element_by_xpath('//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div/label').send_keys(password)
driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()


# In[ ]:


driver.find_element_by_xpath('//*[@id="SearchForm"]/div[2]/div/div/div').send_keys(job)
driver.find_element_by_xpath('//*[@id="SearchForm"]/div[2]/button/span/svg').click()


# In[ ]:


titles = [ x.text for x in title_elements ]
places = [ x.text for x in places_elements ]

