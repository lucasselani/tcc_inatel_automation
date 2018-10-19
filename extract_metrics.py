import data_model
import numpy as np
import scipy.stats

def print_results(metric, data):
    mean, inf_mean, sup_mean, std, avg = mean_confidence_interval(data)
    print(('%s metric:\nmean=%s  inf_mean=%s  sup_mean=%s  std=%s  avg=%s\n\n') \
    % (metric, mean, inf_mean, sup_mean, std, avg))

def std_and_avg(data):
    return np.std(data), np.average(data)

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    std, avg = std_and_avg(a)
    return m, m-h, m+h, std, avg

def metrics(data_list):
    first_contentful_paint_list = []
    first_meaningful_paint_list = []
    speed_index_list = []
    time_to_first_byte_list = []
    first_cpu_idle_list = []
    interactive_list = []
    network_requests_list = []
    total_byte_weight_list = []
    dom_size_list = []

    for data in data_list:
        first_contentful_paint_list.append(data.first_contentful_paint)
        first_meaningful_paint_list.append(data.first_meaningful_paint)
        speed_index_list.append(data.speed_index)
        time_to_first_byte_list.append(data.time_to_first_byte)
        first_cpu_idle_list.append(data.first_cpu_idle)
        interactive_list.append(data.interactive)
        network_requests_list.append(data.network_requests)
        total_byte_weight_list.append(data.total_byte_weight)
        dom_size_list.append(data.dom_size)

    print_results('First contentful paint', first_contentful_paint_list)
    print_results('First meaningful paint', first_meaningful_paint_list)
    print_results('Speed index', speed_index_list)
    print_results('Time to first byte', time_to_first_byte_list)
    print_results('First CPU idle', first_cpu_idle_list)
    print_results('Interactive time', interactive_list)
    print_results('Number of network requests', network_requests_list)
    print_results('Total byte weight', total_byte_weight_list)
    print_results('DOM size', dom_size_list)
