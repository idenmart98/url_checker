from celery.utils import objects
import requests
import time
from .models import Url
from main.celery import app
from celery import group


@app.task()
def check_urls():
    urls = Url.objects.all()
    update_queries = []
    for url in urls:
        try:
            r = requests.get(url)
            if url.status != r.status_code:
                url.status = r.status_code
                update_queries.append(url)
        except requests.exceptions.ConnectionError:
            if url.status != 0:
                url.status = 0
                update_queries.append(url)
    if update_queries:
        Url.objects.bulk_update(update_queries,['status'])        

        



