const http = require('node:http');
const { URL } = require('node:url');

function createStore() {
  return {
    tasks: [
      {
        id: 1,
        title: 'Ship the first safe slice',
        completed: false,
        createdAt: '2026-05-26T00:00:00.000Z'
      }
    ],
    nextId: 2
  };
}

function createTaskService(store) {
  return {
    health() {
      return { ok: true, tasks: store.tasks.length };
    },
    listTasks() {
      return { tasks: store.tasks };
    },
    createTask(body) {
      const title = typeof body.title === 'string' ? body.title.trim() : '';
      if (title.length < 3) {
        return {
          statusCode: 400,
          payload: { error: 'title must be at least 3 characters' }
        };
      }

      const task = {
        id: store.nextId++,
        title,
        completed: false,
        createdAt: new Date().toISOString()
      };
      store.tasks.push(task);
      return { statusCode: 201, payload: { task } };
    },
    completeTask(id) {
      const task = store.tasks.find(item => item.id === id);
      if (!task) {
        return { statusCode: 404, payload: { error: 'task not found' } };
      }
      task.completed = true;
      return { statusCode: 200, payload: { task } };
    }
  };
}

function sendJson(res, statusCode, payload) {
  const body = JSON.stringify(payload);
  res.writeHead(statusCode, {
    'Content-Type': 'application/json; charset=utf-8',
    'Content-Length': Buffer.byteLength(body)
  });
  res.end(body);
}

function readJsonBody(req) {
  return new Promise((resolve, reject) => {
    let raw = '';
    req.on('data', chunk => {
      raw += chunk;
      if (raw.length > 10_000) {
        reject(new Error('payload too large'));
      }
    });
    req.on('end', () => {
      if (!raw) {
        resolve({});
        return;
      }
      try {
        resolve(JSON.parse(raw));
      } catch {
        reject(new Error('invalid json'));
      }
    });
    req.on('error', reject);
  });
}

function createApp() {
  const store = createStore();
  const service = createTaskService(store);

  return http.createServer(async (req, res) => {
    const url = new URL(req.url || '/', 'http://localhost');

    if (req.method === 'GET' && url.pathname === '/health') {
      sendJson(res, 200, service.health());
      return;
    }

    if (req.method === 'GET' && url.pathname === '/api/tasks') {
      sendJson(res, 200, service.listTasks());
      return;
    }

    if (req.method === 'POST' && url.pathname === '/api/tasks') {
      try {
        const body = await readJsonBody(req);
        const result = service.createTask(body);
        sendJson(res, result.statusCode, result.payload);
      } catch (error) {
        sendJson(res, 400, { error: error.message });
      }
      return;
    }

    if (req.method === 'POST' && /^\/api\/tasks\/\d+\/complete$/.test(url.pathname)) {
      const id = Number(url.pathname.split('/')[3]);
      const result = service.completeTask(id);
      sendJson(res, result.statusCode, result.payload);
      return;
    }

    sendJson(res, 404, { error: 'not found' });
  });
}

if (require.main === module) {
  const port = Number(process.env.APP_PORT || 3000);
  const host = process.env.APP_HOST || '127.0.0.1';
  const server = createApp();
  server.listen(port, host, () => {
    console.log(`todo-app-starter listening on http://${host}:${port}`);
  });
}

module.exports = { createApp, createStore, createTaskService };
