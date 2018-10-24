#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data_model
import result_model
import json
import os
import numpy as np
import scipy.stats
import time
import datetime

result = result_model.Result()

def print_results(name, data, metric):
    metric.mean, metric.inf_mean, metric.sup_mean, metric.std\
        = mean_confidence_interval(data)
    return ('%s metric:\nmean=%.5f  inf_mean=%.5f  sup_mean=%.5f  std=%.5f\n') \
        % (name, metric.mean, metric.inf_mean, metric.sup_mean, metric.std)


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h, np.std(a)


def save_results(type_of_rendering):
    path = os.path.dirname(os.path.abspath(__file__)) + \
        (('\\results\\%s_report_%s.json') % (type_of_rendering, int(time.time())))
    with open(path, 'w') as f_json:
		json.dump(result.reprJSON(), f_json)

def metrics(data_list, type_of_rendering, number_of_interactions):
    first_contentful_paint_list = []
    first_meaningful_paint_list = []
    speed_index_list = []
    time_to_first_byte_list = []
    first_cpu_idle_list = []
    interactive_list = []
    network_requests_list = []
    total_byte_weight_list = []
    dom_size_list = []
    number_of_none_results = 0

    for data in data_list:
        if data.first_contentful_paint is not None:
            first_contentful_paint_list.append(data.first_contentful_paint)
        else:
            number_of_none_results = number_of_none_results + 1

        if data.first_meaningful_paint is not None: 
            first_meaningful_paint_list.append(data.first_meaningful_paint)
        else:
            number_of_none_results = number_of_none_results + 1

        if data.speed_index is not None: 
            speed_index_list.append(data.speed_index)
        else:
            number_of_none_results = number_of_none_results + 1

        if data.time_to_first_byte is not None: 
            time_to_first_byte_list.append(data.time_to_first_byte)
        else:
            number_of_none_results = number_of_none_results + 1

        if data.first_cpu_idle is not None: 
            first_cpu_idle_list.append(data.first_cpu_idle)
        else:
            number_of_none_results = number_of_none_results + 1

        if data.interactive is not None:  
            interactive_list.append(data.interactive)
        else:
            number_of_none_results = number_of_none_results + 1

        if data.network_requests is not None: 
            network_requests_list.append(data.network_requests)
        else:
            number_of_none_results = number_of_none_results + 1

        if data.total_byte_weight is not None:
            total_byte_weight_list.append(data.total_byte_weight)
        else:
            number_of_none_results = number_of_none_results + 1

        if data.dom_size is not None:  
            dom_size_list.append(data.dom_size)       
        else:
            number_of_none_results = number_of_none_results + 1     

    path = os.path.dirname(os.path.abspath(__file__)) + \
        (('\\results\\%s_report_%s.txt') % (type_of_rendering, int(time.time())))
    result.report = type_of_rendering
    result.date = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    result.number_of_interactions = len(data_list)
    result.total_number_of_interactions = number_of_interactions
    result.number_of_none_values = number_of_none_results
    with open(path, 'w') as f:
        print >> f, 'Report: %s' % type_of_rendering
        print >> f, 'Date: %s' % datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        print >> f, 'Number of interactions: %s/%s' % (len(data_list), number_of_interactions)
        print >> f, 'Number of None values: %s\n' % number_of_none_results
        print >> f, print_results('First contentful paint', \
            first_contentful_paint_list, result.first_contentful_paint)
        print >> f, print_results('First meaningful paint', \
            first_meaningful_paint_list, result.first_meaningful_paint)
        print >> f, print_results('Speed index', \
            speed_index_list, result.speed_index)
        print >> f, print_results('Time to first byte', \
            time_to_first_byte_list, result.time_to_first_byte)
        print >> f, print_results('First CPU idle', \
            first_cpu_idle_list, result.first_cpu_idle)
        print >> f, print_results('Interactive time', \
            interactive_list, result.interactive)
        print >> f, print_results('Number of network requests', \
            network_requests_list, result.network_requests)
        print >> f, print_results('Total byte weight', \
            total_byte_weight_list, result.total_byte_weight)
        print >> f, print_results('DOM size', \
            dom_size_list, result.dom_size)

    save_results(type_of_rendering)

