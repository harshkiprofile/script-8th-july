from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

driver = webdriver.Chrome()
driver.maximize_window()
df = pd.read_excel('artical websites.xlsx')
for i in range(0,len(df)):
  #try:
    driver.implicitly_wait(10)
    url = 'https://' + df.url[i] + '/'
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_name('username').send_keys(df.User[i])
    driver.find_element_by_name('password').send_keys(df.Password[i])
    driver.find_element_by_class_name('login__').click()
    #time.sleep(8)
    #driver.find_element_by_partial_link_text('My articles').click()
    time.sleep(4)
    driver.get(url + 'create-blog/')
    driver.find_element_by_xpath('//*[@id="blog_title"]').send_keys('This is an awesome blog title')
    driver.find_element_by_xpath('//*[@id="new-blog-desc"]').send_keys('This is an awesome blog description')
    #time.sleep(3)
    driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\Anish\\Downloads\\macbook_wallpaper.jpg")
    #time.sleep(4)
    driver.find_element_by_id('blog_ifr').click()
    actions = ActionChains(driver)
    actions.send_keys("Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit")
    actions.perform()
    select = Select(driver.find_element_by_id('blog_category'))
    select.select_by_value('2')
    driver.find_element_by_class_name('bootstrap-tagsinput').click()
    actions = ActionChains(driver)
    #driver.maximize_window()
    #driver.find_element_by_xpath('/html/body/div[1]/div/a').click()
    actions.send_keys('#trending')
    actions.perform()
    #driver.find_element_by_xpath('//*[@id="insert-blog"]/div[3]/button').click()
    driver.find_element_by_class_name('btn btn-main setting-panel-mdbtn').click()
    time.sleep(5)
    
  #except:
    #print(f'{df.url[i]} skiped... ')
    #continue
