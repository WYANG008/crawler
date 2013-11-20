#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright (c) 2013, Revolution Analytics Singapore.
# All rights reserved.

import json
from WebCrawler.util.logger import setup_logger

logger = setup_logger("Configuration")
ld = logger.debug
le = logger.error


def load_websites(filename):
    """ load the global website configuration.
    """
    configs = None
    with open(filename, 'r') as f:
        configs = json.load(f)
    if not configs:
        le("Error in loading global configuration.")
    if "websites" not in configs.keys():
        le("Error in loading global configuration.")
        return None
    return configs["websites"]
    pass

def load_pages(filename):
    """ load the page configuration for website.
    """
    configs = None
    with open(filename, 'r') as f:
        configs = json.load(f)
    if not configs:
        le("Error in loading global configuration.")
    if "webpages" not in configs.keys():
        le("Error in loading %s webpages configuration." % filename)
        return None
    return configs["webpages"]
    pass

def get_model_config(config, model):
    """
    Get the config for the particular model. 
    """
    for model_config in config:
        for k, v in model_config.iteritems():
            if k == "model" and v == model:
                return model_config
    return None


if __name__ == "__main__":
    pass
