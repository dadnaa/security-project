class NetworkMonitor:
    def __init__(self, network_state):
        self.net = network_state
        self.alerts = []

    def check(self):
        alerts = []

        # ⚠ 1. Downgrade detection
        if self.net.tower == "2G":
            alerts.append("CRITICAL: Network downgraded to 2G")

        # ⚠ 2. Weak encryption detection
        if self.net.encryption == "A5/0":
            alerts.append("CRITICAL: Insecure encryption detected (A5/0)")

        # ⚠ 3. Signal anomaly (fake strong BTS)
        if self.net.signal > -40:
            alerts.append("WARNING: Suspicious strong signal detected (possible Rogue BTS)")

        # store alerts
        self.alerts.extend(alerts)

        return alerts