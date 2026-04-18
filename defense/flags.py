class FlagSystem:
    def __init__(self):
        self.flags = {
            "FLAG_1": False,
            "FLAG_2": False,
            "FLAG_3": False
        }

    def evaluate(self, network_state, alerts):
        # FLAG 1: detect downgrade
        if "2G" in network_state.tower:
            self.flags["FLAG_1"] = True

        # FLAG 2: detect rogue encryption
        if network_state.encryption == "A5/0":
            self.flags["FLAG_2"] = True

        # FLAG 3: detect strong fake signal
        if network_state.signal > -50:
            self.flags["FLAG_3"] = True

        return self.flags

    def show(self):
        print("\n🏁 CTF FLAGS STATUS:")
        for k, v in self.flags.items():
            print(k, "✔" if v else "✖")