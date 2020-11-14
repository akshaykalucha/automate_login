from time import sleep
from selenium import webdriver
import os
from bs4 import BeautifulSoup
import requests
from random import choice
from webdriver_manager.chrome import ChromeDriverManager
import praw
import random
import requests
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import json
from proxydriver import get_chromedriver
from fake_useragent import UserAgent
import schedule
import threading
import time
import re
from multiprocessing import Pool

"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("https://sslproxies.org/")
driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//th[contains(., 'IP Address')]"))))
ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 1]")))]
ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 2]")))]
driver.quit()
proxies = []
for i in range(0, len(ips)):
    proxies.append(ips[i]+':'+ports[i])
print(proxies)
for i in range(0, len(proxies)):
    try:
        print("Proxy selected: {}".format(proxies[i]))
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server={}'.format(proxies[i]))
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        driver.get("https://nordvpn.com/what-is-my-ip/")
        if "Proxy Type" in WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.card-text"))):
            break
    except Exception:
        driver.quit()
print("Proxy Invoked")
"""





def brigade_post(driver, username, password):
        driver.get("https://www.reddit.com/login/")
        login_link = driver.find_element_by_xpath('//*[@id="loginUsername"]')

        login_link.click()


        username_input = driver.find_element_by_css_selector("input[name='username']")
        password_input = driver.find_element_by_css_selector("input[name='password']")


        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/form/div/fieldset[5]/button')

        login_button.click()
        sleep(5)