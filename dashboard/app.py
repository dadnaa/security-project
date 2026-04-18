from flask import Flask, jsonify, render_template_string
import threading
import time

from core.network_state import NetworkState
from attack.rogue_bts import RogueBTS
from attack.downgrade_attack import DowngradeAttack
from attack.imsi_catcher import IMSICatcher

from defense.monitor import NetworkMonitor
from defense.alert_engine import AlertEngine
from defense.flags import FlagSystem

app = Flask(__name__)

# =======================
# GLOBAL SYSTEM STATE
# =======================
net = NetworkState()

rogue = RogueBTS(net)
attack = DowngradeAttack(net)
imsi = IMSICatcher(net)

monitor = NetworkMonitor(net)
alerts = AlertEngine()
flags = FlagSystem()

running = {"attack": False}

# =======================
# ATTACK SEQUENCE THREAD
# =======================
def run_attack():
    running["attack"] = True

    rogue.activate()
    time.sleep(1)

    attack.force_downgrade()
    time.sleep(1)

    imsi.capture()

    # defense run
    detected = monitor.check()
    alerts.trigger(detected)
    flags.evaluate(net, detected)

    running["attack"] = False


# =======================
# API: START ATTACK
# =======================
@app.route("/attack")
def start_attack():
    if not running["attack"]:
        threading.Thread(target=run_attack).start()
    return {"status": "attack started"}


# =======================
# API: SYSTEM STATE
# =======================
@app.route("/status")
def status():
    return jsonify({
        "tower": net.tower,
        "signal": net.signal,
        "encryption": net.encryption,
        "imsi": net.imsi,
        "attacked": net.attacked,
        "alerts": alerts.history[-5:],
        "flags": flags.flags,
        "running": running["attack"]
    })


# =======================
# UI (PHONE DASHBOARD)
# =======================
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>SOC IMSI CATCHER DASHBOARD</title>

<style>
body {
    margin: 0;
    font-family: Arial;
    background: #070b10;
    color: white;
}

/* ===== SOC LAYOUT ===== */
.container {
    display: flex;
    height: 100vh;
}

/* ===== LEFT PHONE ===== */
.phone {
    width: 35%;
    background: #111826;
    padding: 20px;
    border-right: 2px solid #1f2a3a;
    position: relative;
}

.phone.attack {
    animation: redPulse 1s infinite;
}

@keyframes redPulse {
    0% { box-shadow: 0 0 10px red; }
    50% { box-shadow: 0 0 40px red; }
    100% { box-shadow: 0 0 10px red; }
}

/* ===== RIGHT SOC PANEL ===== */
.soc {
    width: 65%;
    padding: 20px;
}

/* ===== CARDS ===== */
.card {
    background: #141c2a;
    padding: 15px;
    margin-bottom: 15px;
    border-radius: 12px;
}

/* ===== ALERTS ===== */
.alert {
    color: orange;
    animation: blink 1s infinite;
}

@keyframes blink {
    50% { opacity: 0.4; }
}

/* ===== STATUS COLORS ===== */
.safe { color: #00ff88; }
.danger { color: red; }

/* ===== LOGS ===== */
.logbox {
    height: 200px;
    overflow-y: auto;
    background: #0c111a;
    padding: 10px;
    font-size: 12px;
}

.log {
    color: #aaa;
    border-bottom: 1px solid #1c2635;
    padding: 3px;
}

/* ===== BUTTON ===== */
button {
    padding: 10px;
    background: red;
    border: none;
    color: white;
    border-radius: 10px;
    cursor: pointer;
}
</style>

</head>

<body>

<div class="container">

<!-- ================= PHONE ================= -->
<div class="phone" id="phone">

    <h2>📱 VICTIM DEVICE</h2>

    <div class="card">
        <p>Network: <span id="tower"></span></p>
        <p>Signal: <span id="signal"></span> dBm</p>
        <p>Encryption: <span id="enc"></span></p>
        <p>IMSI: <span id="imsi"></span></p>

        <p>Status:
            <span id="status"></span>
        </p>
    </div>

    <button onclick="attack()">🔥 Trigger Rogue BTS Attack</button>

</div>

<!-- ================= SOC ================= -->
<div class="soc">

    <h2>🛡️ SOC MONITORING CENTER</h2>

    <!-- ALERTS -->
    <div class="card">
        <h3>🚨 Live Alerts</h3>
        <div id="alerts"></div>
    </div>

    <!-- FLAGS -->
    <div class="card">
        <h3>🏁 CTF Flags</h3>
        <div id="flags"></div>
    </div>

    <!-- LOGS -->
    <div class="card">
        <h3>📡 Attack Timeline</h3>
        <div class="logbox" id="logs"></div>
    </div>

</div>

</div>

<script>

function update(data) {

    // PHONE
    document.getElementById("tower").innerText = data.tower;
    document.getElementById("signal").innerText = data.signal;
    document.getElementById("enc").innerText = data.encryption;
    document.getElementById("imsi").innerText = data.imsi;

    document.getElementById("status").innerText =
        data.attacked ? "COMPROMISED ⚠" : "SECURE";

    document.getElementById("status").className =
        data.attacked ? "danger" : "safe";

    // ALERTS
    document.getElementById("alerts").innerHTML =
        data.alerts.map(a => "<p class='alert'>⚠ " + a + "</p>").join("");

    // FLAGS
    let f = "";
    for (let k in data.flags) {
        f += "<p>" + k + " : " + (data.flags[k] ? "✔" : "✖") + "</p>";
    }
    document.getElementById("flags").innerHTML = f;

    // LOGS (timeline)
    let logs = "";
    data.alerts.forEach((a, i) => {
        logs += "<div class='log'>[" + i + "] " + a + "</div>";
    });
    document.getElementById("logs").innerHTML = logs;

    // ATTACK EFFECT
    let phone = document.getElementById("phone");
    if (data.attacked) {
        phone.classList.add("attack");
    } else {
        phone.classList.remove("attack");
    }
}

async function fetchData() {
    let res = await fetch("/status");
    let data = await res.json();
    update(data);
}

async function attack() {
    await fetch("/attack");
}

setInterval(fetchData, 1000);
fetchData();

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=True, port=5000)