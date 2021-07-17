from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

driver = webdriver.Chrome()
driver.maximize_window()
df = pd.read_excel('artical websites.xlsx')
user_classes = ['username', 'username_email']
login_buttons = ['login__','btn-primary', 'btn-main']
article_texts = ['My articles','My Articles', ' My Articles ', ' My articles ']
# create_texts = ['Add New Article', 'Create', '']
create_text_xpaths = ['//*[@id="contnet"]/div[1]/div/div[2]/div/div[1]/span/a',
'/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div/a',
                      '//*[@id="contnet"]/div[1]/div/div[2]/div[2]/div/div/a']
title_names = ['title' , 'blog_title']
blog_title_xpaths = ['//*[@id="blog_title"]',
                     '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/input']
blog_frame_ids = [ 'blog_ifr', 'text_ifr']
blog_desc_xpaths = ['//*[@id="new-blog-desc"]',]
publish_xpaths = ['//*[@id="insert-blog"]/div[3]/button', 
'/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/button', ]
category_names = ['blog_category', 'category',]
tag_xpaths = ['/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div[5]/div/input',
              '//*[@id="insert-blog"]/div[1]/div[6]/div/div/input',
              '//*[@id="insert-blog"]/div[1]/div[3]/div[2]/div[2]/div/div/input']
#tags_classes = ['bootstrap-tagsinput', 'col-md-10']

for i in range(0,len(df)):
  try:
    # driver.implicitly_wait(2.5)
    url = 'https://' + df.url[i] + '/'
    driver.get(url)
    time.sleep(2)
    
    for user_class in user_classes:
     try:
       driver.find_element_by_name(user_class).send_keys(df.User[i])
     except:
       continue
    driver.find_element_by_name('password').send_keys(df.Password[i])
    
    for login_button in login_buttons:
      try:
       driver.find_element_by_class_name(login_button).click()
      except:
        continue
    time.sleep(4)
    
    for article_text in article_texts:
     try:
      driver.find_element_by_partial_link_text(article_text).click()
     except:
      continue
    time.sleep(2)
    
    for create_text_xpath in create_text_xpaths:
     try:
      # driver.find_element_by_link_text(create_text).click()
      driver.find_element_by_xpath(create_text_xpath).click()
     except:
      continue
    #driver.get(url + 'create-blog/')
    time.sleep(3)
    for blog_title_xpath in blog_title_xpaths:
     try:
      #-------------------Title-----------------------
      # This is to post the blog title
      # Insert the title inside send_keys('')
      # Title should be inside either 'this' or "this"
      # send_keys('the title you wish to post')
      # send_keys("the title you wish to post")
      #-----------------------------------------------
      driver.find_element_by_xpath(blog_title_xpath).send_keys('This is an awesome blog title')
     except:
      continue

    for blog_desc_xpath in blog_desc_xpaths:
     try:
      #---------------Description---------------------
      # This is to post the blog Description
      # Insert the blog Description inside send_keys('')
      # Description must be passed either 'this' or "this"
      # send_keys('the description you wish to post')
      # send_keys("the description you wish to post")
      #-----------------------------------------------
      driver.find_element_by_xpath(blog_desc_xpath).send_keys('This is an awesome blog description')
     except:
      continue
    #time.sleep(3)
      #------------------------Imgae--------------------------
      # This is to post the image for blog
      # Insert the full path to the image inside send_keys('')
      # Path must be passer either inside 'this' or "this"
      # send_keys('Complete path to the image')
      # send_keys("Complete path to the image")
      # if the path contains single back slash \
      # please put double back slashes in all places
      # send_keys('C:\User\documents\my_image.jpg') -> !this is wrong!
      # send_keys("C:\\User\\documents\\my_image.jpg") -> use this one
      #---------------------------------------------------------
    driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\Siddharth\\Desktop\\Scrip article\\8july\\image.jpg")
    #time.sleep(4)
    for blog_frame_id in blog_frame_ids:
     try:
      driver.find_element_by_id(blog_frame_id).click()
      actions = ActionChains(driver)
      #------------------Blog---------------------------------
      # This is to post the complete blog
      # Blog must be passed inside either 'this' or "this"
      # send_keys("My blog")
      # send_keys("My Blog")
      # send_keys("this is a link https://www.google.com/ in my blog")
      #--------------------------------------------------------
      actions.send_keys("Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit")
      actions.perform() 
     except:
      continue
    # actions = ActionChains(driver)
    # actions.send_keys("Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit")
    # actions.perform()

    for category_name in category_names: 
     try:
      select = Select(driver.find_element_by_name(category_name))
      #-----------------category value in integer---------------
      # If you wish to change the blog category
      # go to website
      # find the dropdown to select its category
      # look at which number it is present start counting from 1
      # put the number inside '' or "" pass it to select_by_value
      #---------------------------------------------------------
      select.select_by_value('1')
     except:
       continue 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    for tag_xpath in tag_xpaths:
     try:
      #----------------------Tags----------------------------
      # The tags you want to post for your blog
      # Inside "" or ''
      # send_keys('this_is_trending')
      #------------------------------------------------------
      driver.find_element_by_xpath(tag_xpath).send_keys('trending awesome viral')
      #actions = ActionChains(driver)
      #driver.maximize_window()
      #driver.find_element_by_xpath('/html/body/div[1]/div/a').click()
      #actions.send_keys('#trending')
      #actions.perform()
     except:
      continue 
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    for publish_xpath in publish_xpaths:
     try:
      driver.find_element_by_xpath(publish_xpath).click()
      time.sleep(7)
      print(f'worked on {df.url[i]}')
     except:
       continue 
    #driver.find_element_by_class_name('btn btn-main setting-panel-mdbtn').click()
    if i == len(df)-1:
      driver.close()
    
  except:
    continue
