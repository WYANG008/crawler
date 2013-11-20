#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright (c) 2013, Revolution Analytics
# All rights reserved.

"""
Manage the tasks with Celery.
"""

import os
from WebCrawler.job.tasks import get_data_link 
from WebCrawler.data import database
from WebCrawler.config import config


def start(config_dir):
    """ Start all the process
    """
    websites = config.load_websites(os.path.join(config_dir, "websites.json"))

    for website in websites:
        webconfigs = config.load_pages(os.path.join(config_dir, website["config"]))
        for webconfig in webconfigs:
            if not database.check_table(webconfig["model"]):
                database.initialize_table(webconfig["model"])
        #get_data_link.delay(website["start_url"], website["start_model"], webconfigs)
        get_data_link(website["start_url"], website["start_model"], webconfigs)
    pass


if __name__ == "__main__":
    pass
