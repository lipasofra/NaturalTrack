const express = require('express');
const axios = require('axios');
const app = express();
const port = 3001; // or any other port of your choice

// Proxy endpoint
app.post('/api/v1.0/disasters', async (req, res) => {
  try {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: req.body.query }),
    };

    const response = await axios.post('http://18.217.99.4:8000/api/v1.0/disasters/', requestOptions);

    res.json(response.data);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Something went wrong' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});