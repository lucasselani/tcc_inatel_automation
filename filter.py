class Data:
    method = []
    url = []
    mimeType = []
    sumDNS = 0
    sumWait = 0
    sumSSL = 0
    sumBlocked = 0
    sumConnect = 0
    sumSend = 0
    sumReceive = 0
    totalByte = 0
    numReq = 0
    numExec = 0


def filter(data, numExec):    
    newData = Data()


    ## Verifica quais entries tem o URL https://ssr-vs-csr.herokuapp.com/ssr
    for each_entrie in data['log']['entries']:
        if "https://ssr-vs-csr.herokuapp.com/" in each_entrie['request']['url']:
            print("Method: ", each_entrie['request']['method'])
            newData.method.append(each_entrie['request']['method'])

            print("URL: ", each_entrie['request']['url'])
            newData.url.append(each_entrie['request']['url'])

            print("Response:")

            print("Content Size: ", each_entrie['response']['content']['size'])
            newData.totalByte = newData.totalByte + each_entrie['response']['content']['size']

            print("Content Mimetype: ", each_entrie['response']['content']['mimeType'])
            newData.mimeType.append(each_entrie['response']['content']['mimeType'])

            print("Header Size: ", each_entrie['response']['headersSize'])
            newData.totalByte = newData.totalByte + each_entrie['response']['headersSize']

            print("Body Size: ", each_entrie['response']['bodySize'])
            newData.totalByte = newData.totalByte + each_entrie['response']['bodySize']

            print("Timings [ms]:")

            print("DNS: ", each_entrie['timings']['dns'])
            newData.sumDNS = newData.sumDNS + each_entrie['timings']['dns']

            print("Wait: ", each_entrie['timings']['wait'])
            newData.sumWait = newData.sumWait + each_entrie['timings']['wait']

            print("SSL: ", each_entrie['timings']['ssl'])
            newData.sumSSL = newData.sumSSL + each_entrie['timings']['ssl']

            print("Blocked: ", each_entrie['timings']['blocked'])
            newData.sumBlocked = newData.sumBlocked + each_entrie['timings']['blocked']

            print("Connect: ", each_entrie['timings']['connect'])
            newData.sumConnect = newData.sumConnect + each_entrie['timings']['connect']

            print("Send: ", each_entrie['timings']['send'])
            newData.sumSend = newData.sumSend + each_entrie['timings']['send']

            print("Receive: ", each_entrie['timings']['receive'])
            newData.sumReceive = newData.sumReceive + each_entrie['timings']['receive']

            print("----------------------------------")
            newData.numReq = newData.numReq + 1
            
    newData.numExec = numExec
    ## Salvar o resultado em um novo arquivo JSON
    return newData
   