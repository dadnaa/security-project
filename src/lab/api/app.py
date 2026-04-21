"""Flask app for the IMSI/Rogue BTS Training Lab."""

from __future__ import annotations

from flask import Flask, jsonify, render_template, request

from lab.scenarios.scenario_runner import ScenarioRunner

def create_app(runner: ScenarioRunner | None = None) -> Flask:
    app = Flask(__name__, template_folder="../ui/templates", static_folder="../ui/static")
    scenario_runner = runner or ScenarioRunner()

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/api/status")
    def status():
        return jsonify(scenario_runner.status())

    @app.get("/api/logs")
    def logs():
        return jsonify(scenario_runner.logs())

    @app.post("/api/run/<scenario>")
    def run_scenario(scenario: str):
        result = scenario_runner.run(scenario)
        return jsonify(result)

    @app.post("/api/reset")
    def reset():
        scenario_runner.manager = ScenarioRunner().manager
        return jsonify(scenario_runner.status())

    return app
