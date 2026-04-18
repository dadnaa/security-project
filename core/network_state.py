import random
import time

class NetworkState:
    def __init__(self):
        self.tower = "4G"          # current network
        self.signal = -70          # dBm
        self.encryption = "AES"    # secure by default
        self.imsi = self.generate_imsi()
        self.attacked = False
        self.logs = []

    def generate_imsi(self):
        return "20801" + str(random.randint(100000, 999999))

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.log_state()

    def log_state(self):
        entry = {
            "time": time.time(),
            "tower": self.tower,
            "signal": self.signal,
            "encryption": self.encryption,
            "attacked": self.attacked
        }
        self.logs.append(entry)

    def reset(self):
        self.tower = "4G"
        self.signal = -70
        self.encryption = "AES"
        self.attacked = False
        self.imsi = self.generate_imsi()
        self.logs = []