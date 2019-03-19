﻿import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(path)
# option.add_argument('headless')
# 使用有option的driver可以不顯示視窗
# webdriver.Chrome(chrome_options=option)
# driver = driver.Chrome(chrome_options=option)
# driver = webdriver.browser = webdriver.Remote(
#             command_executor='http://127.0.0.1:4444/wd/hub',
#             desired_capabilities=option.to_capabilities(),)

driver.get("https://www.twitch.tv/directory/game/League%20of%20Legends")

start_text = '//*[@id="root"]/div/div[2]/div/main/div/div[3]/div/div/div/div[3]/div[1]/div/div[1]/p'
element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, start_text)))
driver.find_element_by_xpath(start_text).click()
i = 1
while i < 5:
    url_xpath = '//*[@id="root"]/div/div[2]/div/main/div/div[3]/div/div/div/div[4]/div/div[1]/div[2]/div[' + str(
        i) + ']/div/div/div/div[2]/div[2]/div[1]/a'

    title_xpath = '//*[@id="root"]/div/div[2]/div/main/div/div[3]/div/div/div/div[4]/div/div[1]/div[2]/div[' + str(
        i) + ']/div/div/div/div[2]/div[2]/div[1]/a/h3'
    tt = '//*[@id="root"]/div/div[2]/div/main/div/div[3]/div/div/div/div[4]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/a/h3'
    try:

        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, title_xpath)))
        d = driver.find_element_by_xpath(title_xpath)
        e = driver.find_element_by_xpath(url_xpath)
        print('%s' % (i),d.get_attribute('title'),e.get_attribute("href"))
        i += 1


    except:

        print('等待超時，刷新重來。')
        driver.refresh()
        start_text = '//*[@id="root"]/div/div[2]/div/main/div/div[3]/div/div/div/div[3]/div[1]/div/div[1]/p'
        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, start_text)))
        driver.find_element_by_xpath(start_text).click()
        for cc in range(i):
            ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()

driver.close()
driver.quit()
