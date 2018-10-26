#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import data_model
import os

def filter_results(index_of_execution, type_of_rendering):
    data = data_model.Data()
    path = os.path.dirname(os.path.abspath(__file__)) + \
      (('\\report\\%s_report_%s.json') % (type_of_rendering, index_of_execution))
    with open(path, 'r') as f:
		  json_data = json.load(f)

    data.first_contentful_paint = json_data['audits']['first-contentful-paint']['rawValue']
    data.first_meaningful_paint = json_data['audits']['first-meaningful-paint']['rawValue']
    data.speed_index = json_data['audits']['speed-index']['rawValue']
    data.time_to_first_byte = json_data['audits']['time-to-first-byte']['rawValue']
    data.first_cpu_idle = json_data['audits']['first-cpu-idle']['rawValue']
    data.interactive = json_data['audits']['interactive']['rawValue']
    data.network_requests = json_data['audits']['network-requests']['rawValue']
    data.total_byte_weight = json_data['audits']['total-byte-weight']['rawValue']
    data.dom_size = json_data['audits']['dom-size']['rawValue']
    data.bootup_time = data.interactive = json_data['audits']['bootup-time']['rawValue']
    data.validate()

    return data
