import json
import importlib
import numpy as np


## Abre o arquivo JSON
with open("data.json") as input_file:
    data = json.load(input_file)



dados = []
i = 0
sumDNS = 0
sumWait = 0
sumSSL = 0
sumBlocked = 0
sumConnect = 0
sumSend = 0
sumReceive = 0
totalByte = 0

## Verifica quais entries tem o URL https://ssr-vs-csr.herokuapp.com/ssr
for each_entrie in data['log']['entries']:
    if "https://ssr-vs-csr.herokuapp.com/" in each_entrie['request']['url']:
        print("Method: ", each_entrie['request']['method'])
        dados.append(each_entrie['request']['method'])

        print("URL: ", each_entrie['request']['url'])
        dados.append(each_entrie['request']['url'])

        print("Request:")

        print("Header Size: ", each_entrie['request']['headersSize'])
        ##dados.append(each_entrie['request']['headersSize'])
        totalByte = totalByte + each_entrie['request']['headersSize']

        print("Body Size: ", each_entrie['request']['bodySize'])
        ##dados.append(each_entrie['request']['bodySize'])
        totalByte = totalByte + each_entrie['request']['bodySize']

        print("Response:")

        print("Content Size: ", each_entrie['response']['content']['size'])
        ##dados.append(each_entrie['response']['content']['size'])
        totalByte = totalByte + each_entrie['response']['content']['size']

        print("Content Mimetype: ", each_entrie['response']['content']['mimeType'])
        ##dados.append(each_entrie['response']['content']['mimeType'])

        print("Header Size: ", each_entrie['response']['headersSize'])
        ##dados.append(each_entrie['response']['headersSize'])
        totalByte = totalByte + each_entrie['response']['headersSize']

        print("Body Size: ", each_entrie['response']['bodySize'])
        ##dados.append(each_entrie['response']['bodySize'])
        totalByte = totalByte + each_entrie['response']['bodySize']

        print("Timings [ms]:")

        print("DNS: ", each_entrie['timings']['dns'])
        ##dados.append(each_entrie['timings']['dns'])
        sumDNS = sumDNS + each_entrie['timings']['dns']

        print("Wait: ", each_entrie['timings']['wait'])
        ##dados.append(each_entrie['timings']['wait'])
        sumWait = sumWait + each_entrie['timings']['wait']

        print("SSL: ", each_entrie['timings']['ssl'])
        ##dados.append(each_entrie['timings']['ssl'])
        sumSSL = sumSSL + each_entrie['timings']['ssl']

        print("Blocked: ", each_entrie['timings']['blocked'])
        ##dados.append(each_entrie['timings']['blocked'])
        sumBlocked = sumBlocked + each_entrie['timings']['blocked']

        print("Connect: ", each_entrie['timings']['connect'])
        ##dados.append(each_entrie['timings']['connect'])
        sumConnect = sumConnect + each_entrie['timings']['connect']

        print("Send: ", each_entrie['timings']['send'])
        ##dados.append(each_entrie['timings']['send'])
        sumSend = sumSend + each_entrie['timings']['send']

        print("Receive: ", each_entrie['timings']['receive'])
        ##dados.append(each_entrie['timings']['receive'])
        sumReceive = sumReceive + each_entrie['timings']['receive']

        print("----------------------------------")
        i = i + 1
        


        print(dados)


print("Tempo DNS", sumDNS)
dados.append(sumDNS)


sumTotal = sumDNS + sumBlocked + sumConnect + sumReceive + sumSend + sumSSL + sumSSL + sumWait
print("Tempo total: ", sumTotal)
dados.append(sumTotal)

print("Total de bytes trafegados: ", totalByte)
dados.append(totalByte)
print(i)

## Salvar o resultado em um novo arquivo JSON
with open('new_data.json', 'w') as input_file:
    json.dump(dados, input_file)     
   