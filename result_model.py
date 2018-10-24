import json

class Metric:
    def __init__(self):
        self.std = 0
        self.mean = 0
        self.inf_mean = 0
        self.sup_mean = 0

    def reprJSON(self):
        return dict(std=self.std, mean=self.mean, inf_mean=self.inf_mean, sup_mean=self.sup_mean) 

class Result:
    def __init__(self):
        self.report = ''
        self.date = ''
        self.number_of_interactions = 0
        self.total_number_of_interactions = 0
        self.number_of_none_values = 0
        self.first_contentful_paint = Metric().reprJSON()
        self.first_meaningful_paint = Metric().reprJSON()
        self.speed_index = Metric().reprJSON()
        self.time_to_first_byte = Metric().reprJSON()
        self.first_cpu_idle = Metric().reprJSON()
        self.interactive = Metric().reprJSON()
        self.network_requests = Metric().reprJSON()
        self.total_byte_weight = Metric().reprJSON()
        self.dom_size = Metric().reprJSON()

    def reprJSON(self):
        return dict(report = self.report,\
            date=self.date,\
            number_of_interactions=self.number_of_interactions,\
            total_number_of_interactions=self.total_number_of_interactions,\
            number_of_none_values=self.number_of_none_values,\
            first_contentful_paint=self.first_contentful_paint,\
            first_meaningful_paint=self.first_meaningful_paint,\
            speed_index=self.speed_index,\
            time_to_first_byte=self.time_to_first_byte,\
            first_cpu_idle=self.first_cpu_idle,\
            interactive=self.interactive,\
            network_requests=self.network_requests,\
            total_byte_weight=self.total_byte_weight,\
            dom_size=self.dom_size)