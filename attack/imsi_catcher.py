import random

class IMSICatcher:
    def __init__(self, network_state):
        self.net = network_state

    def capture(self):
        print("[IMSI CATCHER] Attempting capture...")

        if self.net.tower == "2G":
            imsi = "20801" + str(random.randint(100000, 999999))

            self.net.imsi = imsi

            print("[SUCCESS] IMSI captured:", imsi)
            return imsi
        else:
            print("[FAILED] Secure network detected")
            return None