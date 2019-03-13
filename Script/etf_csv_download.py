#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')


# In[3]:


filename = "./Emerging_Markets_ETF_List.csv"
df = pd.read_csv(filename)
for symbol in df['Symbol']:
    print(symbol)
    url = 'https://www.invesco.com/portal/site/us/financial-professional/etfs/product-detail?productId=' + symbol
    driver.get(url)
    element = driver.find_element_by_id('risk-disclosure')
    text = element.find_element_by_tag_name('div').text
    if "No results found." in text: 
        print("===> skip")
    else:
        print("===> download")
        element = driver.find_element_by_id("downloadNavHistory")
        element.click()


# In[ ]:




