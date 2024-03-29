class Data:
    def __init__(self):
        self.first_contentful_paint = 0
        self.first_meaningful_paint = 0
        self.speed_index = 0
        self.time_to_first_byte = 0
        self.first_cpu_idle = 0
        self.interactive = 0
        self.network_requests = 0
        self.total_byte_weight = 0
        self.dom_size = 0
        self.bootup_time = 0
        self.is_valid = True
    
    def validate(self):
        for var in vars(self).itervalues():
            if var is None or var is 0:
                self.is_valid = False