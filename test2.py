from browsermobproxy import Server
from selenium import webdriver
import os
import psutil
import time
import json
import filter

number_of_interactions = 3
filtered_results = []
CHROME = 'Chrome'
FIREFOX = 'Firefox'
BASE_URL = "http://localhost:8000"
CSR_URL = BASE_URL + "/csr"
SSR_URL = BASE_URL + "/ssr"

def open_server(browser):
    for proc in psutil.process_iter():
        if proc.name() == "browsermob-proxy":
            proc.kill()

    dict = {'port': 8090}
    # acha onde ta o jar do browsermod
    path = os.path.dirname(os.path.abspath(__file__)) + \
        "\\browsermob\\bin\\browsermob-proxy"
    # cria o servidor passando onde ta o server e a porta
    server = Server(path=path, options=dict)
    server.start()  # starta o server
    time.sleep(1)
    # cria o proxy que vai ficar "ouvindo" cada request HTTP
    proxy = server.create_proxy()
    time.sleep(1)
    driver = None
    if browser is CHROME:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
        driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        profile = webdriver.FirefoxProfile()
        selenium_proxy = proxy.selenium_proxy()
        profile.set_proxy(selenium_proxy)
        driver = webdriver.Firefox(firefox_profile=profile)
    return driver, proxy, server


def kill_server(driver, server):
    server.stop()
    driver.quit()
    time.sleep(1)


def main():
    for x in range(0, number_of_interactions):
        driver, proxy, server = open_server(CHROME)
        proxy.new_har("TCC")
        driver.get(SSR_URL)
        data = filter.filter(proxy.har, x, BASE_URL)
        #json_data = json.dumps(data.__dict__)
        filtered_results.append(data)
        kill_server(driver, server)
	## Salvar o resultado em um novo arquivo JSON
	#with open('chrome_data.json', 'w') as input_file:
	#	json.dump(filtered_results, input_file)


if __name__ == '__main__':
    main()
