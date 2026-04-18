from core.network_state import NetworkState

net = NetworkState()

print("Initial State:")
print(net.__dict__)

net.update(tower="2G", signal=-40, encryption="A5/0", attacked=True)

print("\nAfter update:")
print(net.__dict__)