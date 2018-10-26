#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please, make sure you have node/npm installed and the ligthouse node module
# To install lighthouse, use: npm install lighthouse -g

import filter_audit as filter
import extract_metrics as extract
import time
import os
import glob
import sys

CSR = 'csr'
SSR = 'ssr'
CSR_URL = 'https://client-side-app.herokuapp.com/'
SSR_URL = 'https://server-side-app.herokuapp.com/'
NUMBER_OF_INTERACTIONS = 100

def clean_folders():
    path = os.path.dirname(os.path.abspath(__file__)) + '\\report\*'
    files = glob.glob(path)
    for f in files:
        os.remove(f)

def execute_lighthouse(url, type_of_rendering, index):
    time.sleep(1)
    os.system(('lighthouse %s --output json\
        --output-path=./report/%s_report_%s.json\
        --config-path=./config.js')\
        % (url, type_of_rendering, index)) 
    path = os.path.dirname(os.path.abspath(__file__)) + \
        (('\\report\\%s_report_%s.json') % (type_of_rendering, index))
    return os.path.isfile(path)

def loop_through(i, ssr_url = SSR_URL, csr_url = CSR_URL):
    ssr_filtered_results = []
    csr_filtered_results = []

    for x in range(0, i):
        success = False
        while not success:
            success = execute_lighthouse(ssr_url, SSR, x)
            
        success = False
        while not success:
            success = execute_lighthouse(csr_url, CSR, x)
        
        ssr_results = filter.filter_results(x, SSR)
        if ssr_results.is_valid:
            ssr_filtered_results.append(ssr_results)

        csr_results = filter.filter_results(x, CSR)
        if csr_results.is_valid:
            csr_filtered_results.append(csr_results)

    return ssr_filtered_results, csr_filtered_results

def test(interactions=NUMBER_OF_INTERACTIONS):
    ssr_results, csr_results = loop_through(interactions) 
    extract.metrics(ssr_results, SSR, interactions)
    extract.metrics(csr_results, CSR, interactions)

def main():
    clean_folders()
    test() if len(sys.argv) == 1 else test(int(sys.argv[1]))

if __name__ == '__main__':
    main()
