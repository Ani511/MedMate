# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

def dummy_job():
    print(f"[Scheduler Ping] {datetime.now()} - Scheduler is active ✅")

scheduler = BackgroundScheduler()
scheduler.add_job(dummy_job, "interval", seconds=30)
scheduler.start()
