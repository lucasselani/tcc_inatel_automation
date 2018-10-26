import json

class Metric:
    def __init__(self):
        self.std = 0
        self.mean = 0
        self.inf_mean = 0
        self.sup_mean = 0

class Result:
    def __init__(self):
        self.report = ''
        self.date = ''
        self.number_of_interactions = 0
        self.total_number_of_interactions = 0
        self.number_of_none_values = 0
        self.first_contentful_paint = vars(Metric())
        self.first_meaningful_paint = vars(Metric())
        self.speed_index = vars(Metric())
        self.time_to_first_byte = vars(Metric())
        self.first_cpu_idle = vars(Metric())
        self.interactive = vars(Metric())
        self.network_requests = vars(Metric())
        self.total_byte_weight = vars(Metric())
        self.dom_size = vars(Metric())
        self.bootup_time = vars(Metric())