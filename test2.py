from browsermobproxy import Server
from selenium import webdriver
import os
import psutil
import time
import json

for proc in psutil.process_iter():
        if proc.name() == "browsermob-proxy":
                proc.kill()

dict = {'port': 8090}
path = os.path.dirname(os.path.abspath(__file__)) + "\\browsermob\\bin\\browsermob-proxy"
server = Server(path=path, options=dict)
server.start()
time.sleep(1)
proxy = server.create_proxy()
time.sleep(1)

profile = webdriver.FirefoxProfile()
selenium_proxy = proxy.selenium_proxy()
profile.set_proxy(selenium_proxy)
driver = webdriver.Firefox(firefox_profile=profile)

proxy.new_har("google")
driver.get("https://ssr-vs-csr.herokuapp.com/ssr")
with open('data.json', 'w') as outfile:
        json.dump(proxy.har, outfile)

server.stop()
driver.quit()