import schedule
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from proxydriver import get_chromedriver
from fake_useragent import UserAgent
import json
from Main import brigade_post

threads = []

def redd_bot(ip, host, uname, passw, typpe="d"):
    print(typpe)
    ua = UserAgent()
    userAgent = ua.random
    browser = get_chromedriver(ip, host, uname, passw, use_proxy=True, user_agent=userAgent)
    return browser
 
def run_threaded():
    with open('data.json', 'r') as f:
        dic = json.load(f)
        shar = dic["shar"]
    for i in range(len(shar)):
        info = shar[i]
        ip, host, uname, passw, ruser, rpass = info["ip"], info["host"], info["uname"], info["passw"], info["ruser"], info["rpass"]
        print(ip,host,uname,passw,ruser,rpass)
        mybot = redd_bot(ip, host, uname, passw)
        job_thread = threading.Thread(target=brigade_post, args=(mybot, ruser, rpass, ))
        # time.sleep(2)
        job_thread.start()
        threads.append(job_thread)
run_threaded()