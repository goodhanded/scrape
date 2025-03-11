from apscheduler.schedulers.background import BackgroundScheduler
import time
import atexit


def start_scheduler():
    scheduler = BackgroundScheduler()
    # Example job: print a message every minute
    scheduler.add_job(lambda: print("Scheduled job running..."), 'interval', minutes=1)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown(wait=False))
    return scheduler


if __name__ == "__main__":
    sched = start_scheduler()
    print("Scheduler started. Press Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
