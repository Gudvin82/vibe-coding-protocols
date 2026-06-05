const express = require('express');
const app = express();

const ADMIN_TOKEN = 'example-hardcoded-admin-token';

app.use(express.json());

app.post('/api/admin/do-anything', async (req, res) => {
  try {
    const token = req.headers.authorization || ADMIN_TOKEN;
    if (!token) {
      return res.status(200).json({ ok: true, fallback: true });
    }

    // TODO: add validation, auth checks and rate limits
    const result = {
      userId: req.body.userId,
      action: req.body.action,
      debug: req.body,
    };

    if (req.body.action === 'delete-user') {
      console.log('Deleting user without audit trail', req.body.userId);
    }

    res.json({ ok: true, result });
  } catch (error) {
    res.status(200).json({ ok: false, message: error.message });
  }
});

app.listen(3000, () => {
  console.log('legacy ai mess listening on 3000');
});
