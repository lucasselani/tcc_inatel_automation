#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please, make sure you have node/npm installed and the ligthouse node module
# To install lighthouse, use: npm install lighthouse -g

import filter_audit as filter
import extract_metrics as extract
import constants
import time
import os
import glob
import sys
from collections import defaultdict

def clean_folders():
    path = os.path.dirname(os.path.abspath(__file__)) + '\\report\*'
    files = glob.glob(path)
    for f in files:
        os.remove(f)

def execute_lighthouse(url, name, index):
    time.sleep(0.2)
    os.system(('lighthouse %s --output json\
        --output-path=./report/%s_report_%s.json\
        --config-path=./config.js')\
        % (url, name, index)) 
    path = os.path.dirname(os.path.abspath(__file__)) + \
        (('\\report\\%s_report_%s.json') % (name, index))
    return os.path.isfile(path)

def loop_through(interactions):
    filtered_results = defaultdict(list)

    for interaction in range(0, interactions):
        for index in range(0, constants.QUANTITY):
            success = False
            while not success:
                success = execute_lighthouse\
                    (constants.URLS[index], constants.NAMES[index], interaction)
        
            results = filter.filter_results(interaction, constants.NAMES[index])
            if results.is_valid:
                filtered_results[index].append(results)

    return filtered_results

def test(interactions=constants.NUMBER_OF_INTERACTIONS):
    results = loop_through(interactions) 
    for index in range(0, constants.QUANTITY):
        extract.metrics(results[index], constants.NAMES[index], interactions)

def main():
    clean_folders()
    test() if len(sys.argv) == 1 else test(int(sys.argv[1]))

if __name__ == '__main__':
    main()
