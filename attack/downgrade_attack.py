import time

class DowngradeAttack:
    def __init__(self, network_state):
        self.net = network_state

    def force_downgrade(self):
        print("[ATTACK] Forcing network downgrade...")

        time.sleep(1)

        # Step 1: LTE rejected
        self.net.update(tower="3G", signal=-60)

        time.sleep(1)

        # Step 2: final drop to insecure 2G
        self.net.update(
            tower="2G",
            signal=-45,
            encryption="A5/0"
        )

        print("[ATTACK] Downgrade complete → 2G insecure mode")