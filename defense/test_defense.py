from core.network_state import NetworkState
from attack.rogue_bts import RogueBTS
from attack.downgrade_attack import DowngradeAttack
from attack.imsi_catcher import IMSICatcher

from defense.monitor import NetworkMonitor
from defense.alert_engine import AlertEngine
from defense.flags import FlagSystem

# system init
net = NetworkState()

rogue = RogueBTS(net)
attack = DowngradeAttack(net)
imsi = IMSICatcher(net)

monitor = NetworkMonitor(net)
alerts = AlertEngine()
flags = FlagSystem()

# 🔥 ATTACK PHASE
rogue.activate()
attack.force_downgrade()
imsi.capture()

# 🛡️ DEFENSE PHASE
detected = monitor.check()
alerts.trigger(detected)
flags.evaluate(net, detected)
flags.show()

print("\nFINAL NETWORK STATE:")
print(net.__dict__)