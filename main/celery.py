import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
if not ("DJANGO_SETTINGS_MODULE" in os.environ):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery('main')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
app.conf.task_always_eager = False
app.conf.beat_schedule = {
    'everyday-task': {
        'task': 'checker.tasks.check_urls',
        'schedule': crontab(hour=0, minute=0), 
    },
}




@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
