from browsermobproxy import Server
from selenium import webdriver
import os
import psutil
import time
import json
# import filter

for proc in psutil.process_iter():
        if proc.name() == "browsermob-proxy":
                proc.kill()

dict = {'port': 8090}
path = os.path.dirname(os.path.abspath(__file__)) + "\\browsermob\\bin\\browsermob-proxy" ##acha onde tá o jar do browsermod
server = Server(path=path, options=dict) ##cria o servidor passando onde tá o server e a porta
server.start() ##starta o server
time.sleep(1) 
proxy = server.create_proxy() ## cria o proxy que vai ficar "ouvindo" cada request HTTP
time.sleep(1)

profile = webdriver.FirefoxProfile() 
selenium_proxy = proxy.selenium_proxy()
profile.set_proxy(selenium_proxy)
driver = webdriver.Firefox(firefox_profile=profile)

for x in range(0,3):
        proxy.new_har("TCC")
        driver.get("https://ssr-vs-csr.herokuapp.com/csr")
        with open('data.har', 'w') as outfile:
                json.dump(proxy.har, outfile)



server.stop()
driver.quit()