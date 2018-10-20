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
CSR_URL = 'http://client-side-app.herokuapp.com/'
SSR_URL = 'http://server-side-app.herokuapp.com/'
number_of_interactions = 100

def loop_through(i=number_of_interactions):
    ssr_filtered_results = []
    csr_filtered_results = []

    for x in range(0, i):
        os.system(('lighthouse %s --output json --output-path=./report/%s_report_%s.json')\
            % (SSR_URL, CSR, x)) 
        time.sleep(1)
        ssr_filtered_results.append(filter.filter_results(x, CSR))
        time.sleep(1)

    for x in range(0, i):
        os.system(('lighthouse %s --output json --output-path=./report/%s_report_%s.json')\
            % (CSR_URL, SSR, x)) 
        time.sleep(1)
        csr_filtered_results.append(filter.filter_results(x, SSRs))
        time.sleep(1)

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
