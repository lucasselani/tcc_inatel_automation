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
    metric['mean'], metric['inf_mean'], metric['sup_mean'], metric['std'], metric['variation']\
        = mean_confidence_interval(data)
    return metric

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h, np.std(a), h

def save_results(type_of_rendering):
    path = os.path.dirname(os.path.abspath(__file__)) + \
        (('\\results\\%s_report_%s.json') % (int(time.time()), type_of_rendering))
    with open(path, 'w') as f_json:
		json.dump(vars(result), f_json)

def validate_data(data, list):
    if data is not None:
        list.append(data)
    else:
        result.number_of_none_values = result.number_of_none_values + 1

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
    bootup_time_list = []

    for data in data_list:
        validate_data(data.first_contentful_paint, first_contentful_paint_list)
        validate_data(data.first_meaningful_paint, first_meaningful_paint_list)
        validate_data(data.speed_index, speed_index_list)
        validate_data(data.time_to_first_byte, time_to_first_byte_list)
        validate_data(data.first_cpu_idle, first_cpu_idle_list)
        validate_data(data.interactive, interactive_list)
        validate_data(data.network_requests, network_requests_list)
        validate_data(data.total_byte_weight, total_byte_weight_list)
        validate_data(data.dom_size, dom_size_list)
        validate_data(data.bootup_time, bootup_time_list)

    result.report = type_of_rendering
    result.date = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    result.number_of_interactions = len(data_list)
    result.total_number_of_interactions = number_of_interactions

    result.first_contentful_paint = get_metric_results(first_contentful_paint_list, result.first_contentful_paint)
    result.first_meaningful_paint = get_metric_results(first_meaningful_paint_list, result.first_meaningful_paint)
    result.speed_index = get_metric_results(speed_index_list, result.speed_index)
    result.time_to_first_byte = get_metric_results(time_to_first_byte_list, result.time_to_first_byte)
    result.first_cpu_idle = get_metric_results(first_cpu_idle_list, result.first_cpu_idle)
    result.interactive = get_metric_results(interactive_list, result.interactive)
    result.network_requests = get_metric_results(network_requests_list, result.network_requests)
    result.total_byte_weight = get_metric_results(total_byte_weight_list, result.total_byte_weight)
    result.dom_size = get_metric_results(dom_size_list, result.dom_size)
    result.bootup_time = get_metric_results(bootup_time_list, result.bootup_time)

    save_results(type_of_rendering)

