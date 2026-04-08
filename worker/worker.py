import os
import time
import redis
import json
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv

load_dotenv()

# Connect to Redis and MongoDB
r = redis.from_url(os.getenv('REDIS_URL'))
client = MongoClient(os.getenv('MONGO_URI'))
db = client['aitasks']
tasks_col = db['tasks']

def process_task(task_id, input_text, operation):
    """Process the AI task based on operation type"""
    if operation == 'uppercase':
        return input_text.upper()
    elif operation == 'lowercase':
        return input_text.lower()
    elif operation == 'reverse':
        return input_text[::-1]
    elif operation == 'wordcount':
        count = len(input_text.split())
        return f"Word count: {count}"
    else:
        raise ValueError(f"Unknown operation: {operation}")

def update_task(task_id, status, result='', logs=''):
    """Update task status in MongoDB"""
    tasks_col.update_one(
        {'_id': ObjectId(task_id)},
        {'$set': {'status': status, 'result': result, 'logs': logs}}
    )

print("🐍 Worker started! Waiting for jobs...")

while True:
    try:
        # Block and wait for job from Redis queue (timeout 5s)
        job = r.blpop('bull:tasks:wait', timeout=5)

        if job:
            _, job_id = job
            job_id = job_id.decode()

            # Get job data from Redis
            job_data = r.hgetall(f'bull:tasks:{job_id}')
            if not job_data:
                continue

            data = json.loads(job_data.get(b'data', b'{}'))
            task_id  = data.get('taskId')
            input_text = data.get('inputText')
            operation  = data.get('operation')

            if not task_id:
                continue

            print(f"📋 Processing task {task_id} | op: {operation}")

            # Update status to running
            update_task(task_id, 'running', logs='Task started...')
            time.sleep(1)  # Simulate processing time

            try:
                result = process_task(task_id, input_text, operation)
                update_task(task_id, 'success', result=result, logs='Task completed successfully.')
                print(f"✅ Task {task_id} completed: {result}")
            except Exception as e:
                update_task(task_id, 'failed', logs=str(e))
                print(f"❌ Task {task_id} failed: {e}")

    except Exception as e:
        print(f"⚠️  Worker error: {e}")
        time.sleep(2)
