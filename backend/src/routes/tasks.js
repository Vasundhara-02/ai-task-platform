const router = require('express').Router();
const Task = require('../models/Task');
const auth = require('../middleware/auth');
const Queue = require('bull');
const taskQueue = new Queue('tasks', process.env.REDIS_URL);

router.post('/', auth, async (req, res) => {
  try {
    const { title, inputText, operation } = req.body;
    const task = await Task.create({
      userId: req.userId, title, inputText, operation, status: 'pending'
    });
    await taskQueue.add({ taskId: task._id.toString(), inputText, operation });
    res.status(201).json(task);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

router.get('/', auth, async (req, res) => {
  const tasks = await Task.find({ userId: req.userId }).sort({ createdAt: -1 });
  res.json(tasks);
});

router.get('/:id', auth, async (req, res) => {
  const task = await Task.findOne({ _id: req.params.id, userId: req.userId });
  if (!task) return res.status(404).json({ message: 'Task not found' });
  res.json(task);
});

module.exports = router;
