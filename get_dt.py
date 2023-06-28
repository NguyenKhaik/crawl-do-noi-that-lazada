# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:55:12 2023

@author: KHAI
"""

# =============================================================================
# lay thong tin nguoi comment va noi dung comment trong tung san pham
# =============================================================================

from selenium import webdriver
import numpy as np
import pandas as pd
from time import sleep
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.common.by import By

def close_content_block(driver):
    try:
        sleep(1)
        c = driver.find_element('xpath', '/html/body/div[7]/div/div[2]/div/span')
        c.click()
        print('tat thong bao')
        sleep(1)
    except:
        pass

# lay ten nguoi cmt, noi dung cmt, skuInfo
def get_info_cmt(driver, link):
    driver.get(link)   
    close_content_block(driver)
    count = 1
    name_cmt, content, skuInfo = [], [], []
    
    while 1:
        try:
            print("Trang " + str(count) + "++++++++")
            
            elems_name = driver.find_elements(By.CSS_SELECTOR , ".item .middle")
            name_cmt = [elem.text for elem in elems_name] + name_cmt
            
            elems_content = driver.find_elements(By.CSS_SELECTOR , ".item .item-content .content")
            content = [elem.text for elem in elems_content] + content
            
            elems_skuInfo= driver.find_elements(By.CSS_SELECTOR , ".item .item-content .skuInfo")
            skuInfo = [elem.text for elem in elems_skuInfo] + skuInfo
            
            a = driver.find_element('xpath', '/html/body/div[4]/div/div[10]/div[1]/div[2]/div/div/div')
            a.location_once_scrolled_into_view
            sleep(2)
    
            next_page_cmt = driver.find_element("xpath", "/html/body/div[4]/div/div[10]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button[2]")
            if next_page_cmt.get_property('disabled'):
                break
            else:
                next_page_cmt.click()
                print("Toi trang tiep")
                sleep(2)
                try:
                    close_btn = driver.find_element("xpath", "/html/body/div[7]/div[2]/div") 
                    close_btn.click()
                    print("Dong thong bao")
                    sleep(1)
                except ElementNotInteractableException:
                    continue
                sleep(1)
                count += 1
        except:
            print('Khong co binh luan')
            break
        
    df4 = pd.DataFrame(list(zip(name_cmt , content, skuInfo)), columns = ['name_cmt', 'content','skuInfo'])
    df4.insert(0, "link_item", link)
    return df4   

# =============================================================================
# #test lay cmt
# thu lay ten nguoi cmt, noi dung cmt, next page 
# driver.get(links[1])
# 
# #get name cmt
# elems_name = driver.find_elements(By.CSS_SELECTOR, '.item .middle')
# name_cmt = [ele.text for ele in elems_name]
# 
# elems_content = driver.find_elements(By.CSS_SELECTOR, '.item .item-content .content')
# content = [ele.text for ele in elems_content]
# 
# elems_skuInfo = driver.find_elements(By.CSS_SELECTOR, '.item .item-content .skuInfo')
# skuInfo = [ele.text for ele in elems_skuInfo]
# 
# df4 = pd.DataFrame(list(zip(name_cmt, content, skuInfo)), columns = ['name_cmt', 'content', 'skuInfo'])
# 
# a = driver.find_element('xpath', '/html/body/div[4]/div/div[10]/div[1]/div[2]/div/div/div')
# driver.execute_script(
#     "arguments[0].location_once_scrolled_into_view(location_once_scrolled_into_view({ behavior: 'smooth', block: 'end', inline: 'end' }));", 
#     a
# )
# 
# a.location_once_scrolled_into_view
# 
# next_page_cmt = driver.find_element('xpath', '/html/body/div[4]/div/div[10]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button[2]')
# # module_product_review
# next_page_cmt.click()
# sleep(2)
# close_btn = driver.find_element('xpath', '/html/body/div[7]/div[2]/div')
# close_btn.click()
# 
# count = 1
# name_cmt, content, skuInfo = [], [], []
# while 1:
#     try:
#         print('Crawl Page ' + str(count))
#         elems_name = driver.find_elements(By.CSS_SELECTOR, '.item .middle')
#         name_cmt = [elem.text for elem in elems_name] + name_cmt
# 
#         elems_content = driver.find_elements(By.CSS_SELECTOR, '.item .item-content .content')
#         content = [elem.text for elem in elems_content] + content
# 
#         elems_skuInfo = driver.find_elements(By.CSS_SELECTOR, '.item .item-content .skuInfo')
#         skuInfo = [elem.text for elem in elems_skuInfo] + skuInfo
#         
#         next_page_cmt = driver.find_element('xpath', '/html/body/div[4]/div/div[10]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button[2]')
#         if next_page_cmt.get_property('disabled'):
#             break
#         else:
#             next_page_cmt.click()
#             print('Bấm nút sang trang ')
#             sleep(3)
#             
#             try:
#                 close_btn = driver.find_element('xpath', '/html/body/div[7]/div[2]/div')
#                 close_btn.click()
#                 print('Bấm nút đóng')
#                 sleep(3)
#             except ElementNotInteractableException:
#                 continue
#         
#             sleep(3)
#             count += 1
#     except:
#         break
# 
# df4 = pd.DataFrame(list(zip(name_cmt, content, skuInfo)), columns = ['name_cmt', 'content', 'skuInfo'])
# df4.insert(0, 'link', links[6])
# 
# driver.close()
# =============================================================================
