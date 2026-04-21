from lab.scenarios.scenario_runner import ScenarioRunner

def test_scenarios_run():
    runner = ScenarioRunner()
    for scenario in runner.available_scenarios():
        result = runner.run(scenario)
        assert 'tower' in result
