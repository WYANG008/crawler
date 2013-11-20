"""
This module contains scripts used by ramiserver
"""

import os
import sys
import celery.bin.celeryd
from WebCrawler.job import task_manager

    
def start_celery():
    celery.bin.celeryd.main()

def start_job():
    task_manager.start("../config")
    


