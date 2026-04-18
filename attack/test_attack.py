from core.network_state import NetworkState
from attack.rogue_bts import RogueBTS
from attack.downgrade_attack import DowngradeAttack
from attack.imsi_catcher import IMSICatcher

# init system
net = NetworkState()

# modules
rogue = RogueBTS(net)
attack = DowngradeAttack(net)
imsi = IMSICatcher(net)

# STEP 1 — Rogue BTS appears
rogue.activate()

# STEP 2 — downgrade attack
attack.force_downgrade()

# STEP 3 — IMSI capture
imsi.capture()

print("\nFINAL STATE:")
print(net.__dict__)