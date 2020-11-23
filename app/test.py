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
import random
import string


def gen_string(length: int) -> str:
    return ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for _ in range(length)
    )



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





def printlog(data, outfile):
    """
    :param data: log and print this to stdout
    :param outfile: to fhis file
    :return: -
    """
    pp_json(data)
    with open(outfile, 'a') as log:
        log.write(str(data) + "\n")

class AnagramTest(unittest.TestCase):
    def test_no_matches(self):
        candidates = ["hello", "world", "zombies", "pants"]
        expected = []
        self.assertCountEqual(find_anagrams("diaper", candidates), expected)

    def test_detects_two_anagrams(self):
        candidates = ["stream", "pigeon", "maters"]
        expected = ["stream", "maters"]
        self.assertCountEqual(find_anagrams("master", candidates), expected)

    def test_does_not_detect_anagram_subsets(self):
        candidates = ["dog", "goody"]
        expected = []
        self.assertCountEqual(find_anagrams("good", candidates), expected)

    def test_detects_anagram(self):
        candidates = ["enlists", "google", "inlets", "banana"]
        expected = ["inlets"]
        self.assertCountEqual(find_anagrams("listen", candidates), expected)

    def test_detects_three_anagrams(self):
        candidates = ["gallery", "ballerina", "regally", "clergy", "largely", "leading"]
        expected = ["gallery", "regally", "largely"]
        self.assertCountEqual(find_anagrams("allergy", candidates), expected)

    def test_detects_multiple_anagrams_with_different_case(self):
        candidates = ["Eons", "ONES"]
        expected = ["Eons", "ONES"]
        self.assertCountEqual(find_anagrams("nose", candidates), expected)

    def test_does_not_detect_non_anagrams_with_identical_checksum(self):
        candidates = ["last"]
        expected = []
        self.assertCountEqual(find_anagrams("mass", candidates), expected)

    def test_detects_anagrams_case_insensitively(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        expected = ["Carthorse"]
        self.assertCountEqual(find_anagrams("Orchestra", candidates), expected)

    def test_detects_anagrams_using_case_insensitive_subject(self):
        candidates = ["cashregister", "carthorse", "radishes"]
        expected = ["carthorse"]
        self.assertCountEqual(find_anagrams("Orchestra", candidates), expected)

    def test_detects_anagrams_using_case_insensitive_possible_matches(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        expected = ["Carthorse"]
        self.assertCountEqual(find_anagrams("orchestra", candidates), expected)

    def test_does_not_detect_an_anagram_if_the_original_word_is_repeated(self):
        candidates = ["go Go GO"]
        expected = []
        self.assertCountEqual(find_anagrams("go", candidates), expected)

def check_ip(version, debug, proxy, tor_proxy, proxy_type, outfile):
    """
    :param version: ipv4 or ipv6
    :param debug: don't use headless mode (for debugging)
    :param proxy: use this proxy server
    :param tor_proxy: configure browser for tor proxy
    :param outfile: log to this file
    :return: --
    """
    opts = Options()
    if not debug:
        opts.set_headless()
        assert opts.headless  # Operating in headless mode

    profile = webdriver.FirefoxProfile()
    if not proxy:
        proxy = None
    # set FF preference to socks proxy
    if proxy or tor_proxy:
        _print('Setting proxy...')
        if proxy is not None:
            proxy = proxy.split(':')
            proxy_host = str(proxy[0])
            proxy_port = int(proxy[1])
            _print('Proxy: %s:%d' % (proxy_host, proxy_port))
            profile.set_preference("network.proxy.type", 1)
            if tor_proxy or proxy_type == 'tor':
                profile.set_preference("network.proxy.socks", proxy_host)
                profile.set_preference("network.proxy.socks_port", proxy_port)
                profile.set_preference("network.proxy.socks_version", 5)
                profile.set_preference('network.proxy_dns', 'true')  # Proxy DNS
            elif proxy_type == 'socks5':
                profile.set_preference("network.proxy.socks", proxy_host)
                profile.set_preference("network.proxy.socks_port", proxy_port)
                profile.set_preference("network.proxy.socks_version", 5)
                profile.set_preference('network.proxy_dns', 'true')  # Proxy DNS
            elif proxy_type == 'socks4':
                profile.set_preference("network.proxy.socks", proxy_host)
                profile.set_preference("network.proxy.socks_port", proxy_port)
                profile.set_preference("network.proxy.socks_version", 4)
            elif proxy_type == 'http':
                profile.set_preference("network.proxy.http", proxy_host)
                profile.set_preference("network.proxy.http_port", proxy_port)
                profile.set_preference('network.proxy.https', proxy_host)
                profile.set_preference('network.proxy.https', proxy_port)
                profile.set_preference('network.proxy.ssl', proxy_host)
                profile.set_preference('network.proxy.ssl_port', proxy_port)
                profile.set_preference('network.proxy_dns', 'true')  # Proxy DNS


@bot.command(pass_context = True)
async def report(ctx, user : discord.Member, *reason):

    channel = bot.get_channel(739057829599641630) 

    author = ctx.message.author

    rearray = ' '.join(reason[:]) 

    if not rearray: 
        
        goose = discord.Embed(title = f"{author}{user}", color = (0x6eb3ac))

        await channel.send(embed = goose)

        await ctx.message.delete() 

    else:
        
        goose1 = discord.Embed(title = f"{author}{user}{rearray}", color = (0x6eb3ac))

        await channel.send(embed = goose1)

        await ctx.message.delete()
file = open("insta_followers_of/" + user + ".txt", "a+")
for follower in profile.get_followers():
    username = follower.username
    file.write(username + "\n")
    print(username)
file.close()