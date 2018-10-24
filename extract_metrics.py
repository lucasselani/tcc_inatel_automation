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

def get_metric_results(data, metric):
    metric['mean'], metric['inf_mean'], metric['sup_mean'], metric['std'] = mean_confidence_interval(data)
    return metric

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

    result.report = type_of_rendering
    result.date = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    result.number_of_interactions = len(data_list)
    result.total_number_of_interactions = number_of_interactions
    result.number_of_none_values = number_of_none_results
    result.first_contentful_paint = get_metric_results(first_contentful_paint_list, result.first_contentful_paint)
    result.first_meaningful_paint = get_metric_results(first_meaningful_paint_list, result.first_meaningful_paint)
    result.speed_index = get_metric_results(speed_index_list, result.speed_index)
    result.time_to_first_byte = get_metric_results(time_to_first_byte_list, result.time_to_first_byte)
    result.first_cpu_idle = get_metric_results(first_cpu_idle_list, result.first_cpu_idle)
    result.interactive = get_metric_results(interactive_list, result.interactive)
    result.network_requests = get_metric_results(network_requests_list, result.network_requests)
    result.total_byte_weight = get_metric_results(total_byte_weight_list, result.total_byte_weight)
    result.dom_size = get_metric_results(dom_size_list, result.dom_size)

    save_results(type_of_rendering)

