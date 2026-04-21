"""CLI for the IMSI/Rogue BTS Training Lab."""

from __future__ import annotations

import argparse
import json
from typing import List

from lab.scenarios.scenario_runner import ScenarioRunner
from lab.api.app import create_app

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="lab", description="IMSI/Rogue BTS Training Lab")
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Run a training scenario")
    run.add_argument("scenario", choices=ScenarioRunner.available_scenarios())

    sub.add_parser("status", help="Print current network status")
    sub.add_parser("logs", help="Print recent event logs")

    serve = sub.add_parser("serve", help="Run the web UI and API")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=5000)

    return parser

def main(argv: List[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    runner = ScenarioRunner()

    if args.command == "run":
        result = runner.run(args.scenario)
        print(json.dumps(result, indent=2))
        return

    if args.command == "status":
        print(json.dumps(runner.status(), indent=2))
        return

    if args.command == "logs":
        print(json.dumps(runner.logs(), indent=2))
        return

    if args.command == "serve":
        app = create_app(runner)
        app.run(host=args.host, port=args.port, debug=True)
        return