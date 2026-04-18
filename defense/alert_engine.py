class AlertEngine:
    def __init__(self):
        self.history = []

    def trigger(self, alerts):
        if not alerts:
            return

        print("\n🚨 SECURITY ALERT 🚨")

        for a in alerts:
            print(" -", a)

        self.history.extend(alerts)