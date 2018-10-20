#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please, make sure you have node/npm installed and the ligthouse node module
# To install lighthouse, use: npm install lighthouse -g

import filter_audit as filter
import extract_metrics as extract
import time
import os

CSR = 'csr'
SSR = 'ssr'
CSR_LOCAL = 'http://localhost:5000'
SSR_LOCAL = 'http://localhost:3000'
CSR_URL = 'http://client-side-app.herokuapp.com/'
SSR_URL = 'http://server-side-app.herokuapp.com/'
number_of_interactions = 100

def loop_through(i=number_of_interactions, ssr_url = SSR_URL, csr_url = CSR_URL):
    ssr_filtered_results = []
    csr_filtered_results = []

    for x in range(0, i):
        os.system(('lighthouse %s --output json --output-path=./report/%s_report_%s.json')\
            % (ssr_url, SSR, x)) 
        time.sleep(1)
        os.system(('lighthouse %s --output json --output-path=./report/%s_report_%s.json')\
            % (csr_url, CSR, x)) 
        time.sleep(1)
        
        ssr_filtered_results.append(filter.filter_results(x, SSR))
        csr_filtered_results.append(filter.filter_results(x, CSR))

    return ssr_filtered_results, csr_filtered_results

def mock_test():
    ssr_results, csr_results = loop_through(3)
    extract.metrics(ssr_results, SSR)
    extract.metrics(csr_results, CSR)

def test():
    ssr_results, csr_results = loop_through()
    extract.metrics(ssr_results, SSR)
    extract.metrics(csr_results, CSR)

def main():
    mock_test()

if __name__ == '__main__':
    main()
