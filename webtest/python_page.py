# /usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver="C:\Users\whq\AppData\Local\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://www.python.org/")
JS1="document.title='修改了"
driver.execute_script(JS1)
