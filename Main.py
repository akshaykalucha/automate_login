from time import sleep
from selenium import webdriver
import os
from bs4 import BeautifulSoup
import requests
from random import choice
from webdriver_manager.chrome import ChromeDriverManager
import praw
import pprint
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

'''
def sub():
    threads = []
    with Pool() as pool:
        driver = get_chromedriver()
        thread = threading.Thread(driver.get('https:.....'))
        threads.append(thread)
'''


def brigade_post(driver, username, password):
        driver.get("https://www.reddit.com/login")
        login_link = driver.find_element_by_xpath('//*[@id="loginUsername"]')

        login_link.click()


        username_input = driver.find_element_by_css_selector("input[name='username']")
        password_input = driver.find_element_by_css_selector("input[name='password']")


        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/form/div/fieldset[5]/button')

        login_button.click()
        sleep(5)