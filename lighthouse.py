import filter_audit as filter
import extract_metrics as extract
import time
import os

BASE_URL = 'http://localhost:3000'
CSR_URL = BASE_URL + '/csr'
SSR_URL = BASE_URL + ''
number_of_interactions = 100

def loop_through(i=number_of_interactions):
    filtered_results = []
    for x in range(0, i):
        os.system(('lighthouse %s --output json --output-path=./report/report_%s.json') % (SSR_URL, x)) 
        time.sleep(1)
        filtered_results.append(filter.filter_results(x))
        time.sleep(1)
    return filtered_results

def test():
    results = loop_through(3)
    extract.metrics(results)

def main():
    # print('Please, make sure you have node/npm installed and the ligthouse node module')
    # print('To install lighthouse, use: npm install lighthouse -g')
    # raw_input('Press any key to continue')

    test()

if __name__ == '__main__':
    main()
