import os
import time
import redis
import json
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379')
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongodb:27017/aitasks')

print(f"Connecting to Redis: {REDIS_URL}")
print(f"Connecting to MongoDB: {MONGO_URI}")

r = redis.from_url(REDIS_URL)
client = MongoClient(MONGO_URI)
db = client['aitasks']
tasks_col = db['tasks']

print("✅ Worker started! Waiting for jobs...")

def process_task(input_text, operation):
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
    tasks_col.update_one(
        {'_id': ObjectId(task_id)},
        {'$set': {'status': status, 'result': result, 'logs': logs}}
    )
    print(f"Task {task_id} updated to {status}")

while True:
    try:
        # Try multiple Bull queue key formats
        job = None
        for key in ['bull:tasks:wait', 'bull:tasks:waiting', 'tasks']:
            job = r.blpop(key, timeout=2)
            if job:
                print(f"Found job in key: {key}")
                break

        if job:
            _, job_data = job
            try:
                data = json.loads(job_data)
                task_id = data.get('taskId')
                input_text = data.get('inputText')
                operation = data.get('operation')
            except:
                # Try Bull format
                job_id = job_data.decode()
                raw = r.hgetall(f'bull:tasks:{job_id}')
                if not raw:
                    continue
                data = json.loads(raw.get(b'data', b'{}'))
                task_id = data.get('taskId')
                input_text = data.get('inputText')
                operation = data.get('operation')

            if not task_id:
                print("No taskId found, skipping...")
                continue

            print(f"Processing: {task_id} | {operation} | {input_text}")
            update_task(task_id, 'running', logs='Processing...')
            time.sleep(1)

            try:
                result = process_task(input_text, operation)
                update_task(task_id, 'success', result=result, logs='Completed!')
                print(f"✅ Done: {result}")
            except Exception as e:
                update_task(task_id, 'failed', logs=str(e))
                print(f"❌ Failed: {e}")
        else:
            # Also check pending tasks in MongoDB directly
            pending = tasks_col.find_one({'status': 'pending'})
            if pending:
                task_id = str(pending['_id'])
                input_text = pending.get('inputText', '')
                operation = pending.get('operation', '')
                print(f"Found pending task in DB: {task_id}")
                update_task(task_id, 'running', logs='Processing...')
                time.sleep(1)
                try:
                    result = process_task(input_text, operation)
                    update_task(task_id, 'success', result=result, logs='Completed!')
                    print(f"✅ Done: {result}")
                except Exception as e:
                    update_task(task_id, 'failed', logs=str(e))

    except Exception as e:
        print(f"⚠️ Error: {e}")
        time.sleep(2)
