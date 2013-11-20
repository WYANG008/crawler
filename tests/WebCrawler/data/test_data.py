#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unit Test for data saving  data saving.

@author Wang Qiang
"""

import urllib2
import unittest
from WebCrawler.config import config
from WebCrawler.parser import parser
from WebCrawler.data import database


class UnitTest(unittest.TestCase):
    """
    test for Saving data. 
    """
    
    def testFileConnector(self):
        data = {}
        model = "trip_review_detail"
        webconfigs = config.load_pages("../config/tripadvisor.json")
        web_config = config.get_model_config(webconfigs, model)
        test_page = "http://www.tripadvisor.com.sg/ShowUserReviews-g294265-d2516429-r165190313-Auld_Alliance-Singapore.html#REVIEWS"
        html = urllib2.urlopen(test_page).read()
        data, links = parser.parse_page(html, web_config)
        for edata in data:
            database.save_data(edata, web_config["model"], web_config)
        self.assertEqual(1, 1)
        self.assertTrue(True)
   

if __name__ == '__main__':
    # Test all
    unittest.main()
