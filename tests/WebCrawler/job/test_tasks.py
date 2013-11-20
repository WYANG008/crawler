#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unit Test for WebCrawler.job 

@author Wang Qiang
"""

import sys

sys.path[0:0] = [
    '/home/ec2-user/rr-crawler/src'
]
import unittest
from WebCrawler.job import tasks
from WebCrawler.config import config


class UnitTest(unittest.TestCase):
    """
    Test for WebCrawler.job 
    """
    
    def testTasks(self):
        pages_config = config.load_pages("../config/skyscanner.json")
        model = "skyscanner_flight"
        test_page = "http://www.skyscanner.net/flights-to/lond/cheap-flights-to-london.html"
        tasks.get_data_link(test_page, model, pages_config)
        #tasks.get_data_link(test_page, model, pages_config)
        #print data
        #print links


if __name__ == '__main__':
    # Test all
    unittest.main()

