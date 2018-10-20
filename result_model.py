class Result:
    def __init__(self):
        self.first_contentful_paint = Metric()
        self.first_meaningful_paint = Metric()
        self.speed_index = Metric()
        self.time_to_first_byte = Metric()
        self.first_cpu_idle = Metric()
        self.interactive = Metric()
        self.network_requests = Metric()
        self.total_byte_weight = Metric()
        self.dom_size = Metric()

    class Metric:
        def __init__(self):
            self.avg = 0
            self.std = 0
            self.mean = 0
            self.inf_mean = 0
            self.sup_mean = 0