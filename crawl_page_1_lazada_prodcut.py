# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 19:09:08 2023

@author: KHAI
"""

# =============================================================================
# lay cac thong tin do noi that tu web lazada trong page 1
# =============================================================================


from selenium import webdriver
import numpy as np
import pandas as pd
from time import sleep
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from get_dt import get_info_cmt

# ket noi chromedriver
driver = webdriver.Chrome()

# phong to cua so chrome
driver.maximize_window()

#mo link web va doi hien thi san pham
link_web = 'https://www.lazada.vn/san-pham-noi-that/?spm=a2o4n.searchlistcategory.cate_7.9.68d444afygLqrB'
driver.get(link_web)
sleep(5)

# tim element, lay title, lay link san pham
elems = driver.find_elements(By.CSS_SELECTOR, '.RfADt [href]')
title = [ele.get_attribute('title') for ele in elems]
links = [ele.get_attribute('href') for  ele in elems]

# lay gia san pham
elem_price = driver.find_elements(By.CSS_SELECTOR, '.aBrP0')
price = [ele.text for ele in elem_price]

#tao df luu title, price, link
df1 = pd.DataFrame(list(zip(title, price, links)), columns = ['title', 'price', 'link'])

#danh index cho tung dong
df1['index_'] = np.arange(1, len(df1) + 1)

idx_discount, list_discount = [], []
for i in range (1, len(title)+1):
    try:
        discount_percent = driver.find_element('xpath',f'/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[4]')
        list_discount.append(discount_percent.text)
        print(i)
        idx_discount.append(i)
    except NoSuchElementException:
        print(f"{i} Khong co giam gia")

df2 = pd.DataFrame(list(zip(idx_discount, list_discount)), columns = ['idx_discount', 'list_discount'])

df3 = df1.merge(df2, how = 'left', left_on = 'index_', right_on = 'idx_discount')

# =============================================================================
# area = []
# for i in range(1,41):
#     area_element = driver.find_elements('xpath', f'/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[5]/span[1]')
#     
#     if area_element is not None:
#         for x in area_element:
#             e = 
#             area.append(x.text)
#     else:
#         area.append(' ')
# =============================================================================
# =============================================================================
# elems_sold = driver.find_elements(By.CSS_SELECTOR, '._1cEkb')
# sold = [ele.text for ele in elems_sold]
# 
# elems_review_count = driver.find_elements(By.CSS_SELECTOR, '.qzqFw')
# review_count = [ele.text for ele in elems_review_count]
# 
# elems_rating = driver.find_elements(By.CSS_SELECTOR, '.mdmmT._32vUv')
# rating = [len(ele) for ele in elems_rating]
# =============================================================================

# lay vi tri
elem_review_location = driver.find_elements(By.CSS_SELECTOR, '._6uN7R')
review_location = [ele.text for ele in elem_review_location]

df3['review_location'] = review_location

list_df = []
for link in links:
    print("--------------Product " + str(links.index(link) + 1) + "/" + str(len(links)) + "-----------------")
    df = get_info_cmt(driver, link)
    list_df.append(df)







