const express = require('express');
const mongoose = require('mongoose');
const helmet = require('helmet');
const cors = require('cors');
const rateLimit = require('express-rate-limit');
require('dotenv').config();

const app = express();
app.use(helmet());
app.use(cors());
app.use(express.json());
app.use(rateLimit({ windowMs: 15 * 60 * 1000, max: 100 }));

app.use('/api/auth', require('./routes/auth'));
app.use('/api/tasks', require('./routes/tasks'));

// Health check endpoint
app.get('/health', (req, res) => res.json({ status: 'ok' }));

// Retry MongoDB connection
const connectWithRetry = () => {
  mongoose.connect(process.env.MONGO_URI)
    .then(() => console.log('✅ MongoDB connected'))
    .catch(err => {
      console.error('MongoDB connection failed, retrying in 5s...', err.message);
      setTimeout(connectWithRetry, 5000);
    });
};

connectWithRetry();
app.listen(5000, () => console.log('✅ Server running on port 5000'));
