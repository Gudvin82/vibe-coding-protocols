const express = require('express');

function createConfig(env) {
  return {
    port: Number(env.PORT || 3000),
    adminToken: env.ADMIN_TOKEN || '',
  };
}

function validateAdminAction(body) {
  if (!body || typeof body !== 'object') {
    return 'Body must be JSON.';
  }
  if (typeof body.userId !== 'string' || body.userId.length < 3) {
    return 'userId must be a non-empty string.';
  }
  if (!['disable-user', 'reset-session'].includes(body.action)) {
    return 'action is not allowed.';
  }
  return null;
}

const app = express();
const config = createConfig(process.env);

app.use(express.json());

app.post('/api/admin/do-anything', (req, res) => {
  const authHeader = req.headers.authorization || '';
  if (!config.adminToken || authHeader !== `Bearer ${config.adminToken}`) {
    return res.status(401).json({ ok: false, message: 'Unauthorized.' });
  }

  const validationError = validateAdminAction(req.body);
  if (validationError) {
    return res.status(400).json({ ok: false, message: validationError });
  }

  const result = {
    userId: req.body.userId,
    action: req.body.action,
  };

  return res.json({ ok: true, result });
});

app.listen(config.port, () => {
  console.log(`legacy ai mess hardened example listening on ${config.port}`);
});
