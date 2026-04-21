async function fetchJson(url, options) {
  const resp = await fetch(url, options);
  return await resp.json();
}

async function refresh() {
  const state = await fetchJson('/api/status');
  const logs = await fetchJson('/api/logs');
  document.getElementById('state').textContent = JSON.stringify(state, null, 2);
  document.getElementById('logs').textContent = JSON.stringify(logs, null, 2);
}

async function runScenario(name) {
  await fetchJson(`/api/run/${name}`, { method: 'POST' });
  await refresh();
}

async function resetLab() {
  await fetchJson('/api/reset', { method: 'POST' });
  await refresh();
}

document.querySelectorAll('button[data-scenario]').forEach((btn) => {
  btn.addEventListener('click', () => runScenario(btn.dataset.scenario));
});

document.getElementById('reset').addEventListener('click', resetLab);

refresh();
