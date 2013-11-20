#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright (c) 2013, Revolution Analytics
# All rights reserved.

import time
import redis
import requests
from datetime import timedelta
from WebCrawler.config import config
from WebCrawler.parser import parser
from WebCrawler.data import database
from WebCrawler.util.logger import setup_logger
from celery.utils.log import get_task_logger
from celery import Celery
from urllib2 import HTTPError


logger = get_task_logger("Crawling Job")
ld = logger.debug
le = logger.error


celery = Celery('tasks', broker='redis://localhost', backend='redis://localhost')

# Add lock for multiprocessing
def check_url(url):
    db = redis.Redis(db=0)
    item = db.get(url)
    return item

def set_url_done(url):
    db = redis.Redis(db=0)
    d = timedelta(days=2)
    db.setex(url, "1", d)

def clear_url_done(url):
    db = redis.Redis(db=0)
    d = timedelta(days=2)
    db.setex(url, "", d)

@celery.task(name='WebCrawler.job.tasks.get_data_link')
def get_data_link(url, model, webconfig):
    """
    Fetch data for the task url.
    """
    # check the whether the task is required.
    try:
        have_done = check_url(url)
        if not have_done:
            print url
            r = requests.get(url)
            r.raise_for_status()
            content = r.text
            web_config = config.get_model_config(webconfig, model)
            data, links = parser.parse_page(content, web_config)
            print len(data)
            print len(links)
            # save data
            for edata in data:
                database.save_data(edata, web_config["model"], web_config)
            set_url_done(url)

            # submit new task
            for turl, tModel in links:
                #get_data_link.delay(turl, tModel, webconfig)
                get_data_link(turl, tModel, webconfig)
            return web_config["model"] + str(len(data))
        return "Done"
    except Exception as inst:
        clear_url_done(url)
        return type(inst)


if __name__ == "__main__":
    pass
