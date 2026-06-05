const test = require('node:test');
const assert = require('node:assert/strict');
const { createStore, createTaskService } = require('../src/index.js');

test('todo app starter health and task flow', () => {
  const service = createTaskService(createStore());

  const health = service.health();
  assert.equal(health.ok, true);
  assert.equal(typeof health.tasks, 'number');

  const listBefore = service.listTasks();
  assert.equal(Array.isArray(listBefore.tasks), true);
  const startCount = listBefore.tasks.length;

  const created = service.createTask({ title: 'Write a smoke test' });
  assert.equal(created.statusCode, 201);
  assert.equal(created.payload.task.completed, false);

  const completed = service.completeTask(created.payload.task.id);
  assert.equal(completed.statusCode, 200);
  assert.equal(completed.payload.task.completed, true);

  const listAfter = service.listTasks();
  assert.equal(listAfter.tasks.length, startCount + 1);

  const invalid = service.createTask({ title: 'x' });
  assert.equal(invalid.statusCode, 400);
});
