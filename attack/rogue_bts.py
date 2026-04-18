import random
import time

class RogueBTS:
    def __init__(self, network_state):
        self.net = network_state
        self.active = False

    def broadcast(self):
        # Fake very strong signal to attract phone
        return {
            "tower": "4G",
            "signal": -30,   # stronger than real towers
            "fake_auth": True
        }

    def activate(self):
        print("[ROGUE BTS] Activated")
        self.active = True

        # spoof attraction
        signal = self.broadcast()

        self.net.update(
            tower=signal["tower"],
            signal=signal["signal"],
            attacked=True
        )