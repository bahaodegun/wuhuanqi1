# /usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver="C:\Users\whq\AppData\Local\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.maximize_window() #浏览器最大化
#隐形等待
#driver.implicitly_wait(30)

driver.get("http://39.156.1.70:81/")#登录咪咕系统
#用户名定位
user_xpath='//div[@class="col-md-12"]//input[@type="text"]'
#等待元素出现，出现后点击
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,user_xpath)))
driver.find_element_by_xpath(user_xpath).send_keys("15882279916")
#密码栏定位
pwd_xpath='//div[@class="col-md-12"]//input[@type="password"]'
#等待元素出现，出现后点击
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,pwd_xpath)))
driver.find_element_by_xpath(pwd_xpath).send_keys("wuhuanqi1")

#确认按钮定位
button_xpath='//button[@class="btn btn-lg btn-login btn-block"]'
#等待元素出现，出现后点击
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,button_xpath)))
driver.find_element_by_xpath(button_xpath).click()
#退出按钮定位

quit_log='//i[@class="fa fa-sign-out"]'



#系统管理按钮定位
system_button='//span[@class="fa fa-cog"]'
#等待元素出现，出现后点击
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,system_button)))
driver.find_element_by_xpath(system_button).click()

#角色管理定位
role_manage='//i[@class="fa fa-vcard"]'
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,role_manage)))
driver.find_element_by_xpath(role_manage).click()

#新建角色定位
new_role='//a[@class="btn btn-primary toolbar-add toolbar-add"]'
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,new_role)))
driver.find_element_by_xpath(new_role).click()

#截图
driver.save_screenshot('test_photo\\bing_1.png')

#关闭浏览器
driver.quit()


