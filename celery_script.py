from celery import Celery
from celery.schedules import crontab
from crawler import run_crawler
app = Celery('celery_script', broker = 'redis://localhost')

app.conf.timezone = 'UTC'

@app.task
def celery_beat_crawler():
    run_crawler()

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'celery_script.celery_beat_crawler',
        'schedule': 30.0, # 60 Seconds
        #'args': ('testing'),
    },
}