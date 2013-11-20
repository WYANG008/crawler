#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unit Test for config.config.py 

@author Wang Qiang
"""
import unittest
from WebCrawler.config import config

import urllib
import urllib2
import HTMLParser

from lxml.cssselect import CSSSelector
from lxml.html import fromstring
from lxml import etree


class UnitTest(unittest.TestCase):
    """
    test for config
    """

    def testLoadWebSite(self):
        websites = config.load_websites("./websites.json")
        print len(websites)
        pass
    
    def testLoadWebPages(self):
        webpages = config.load_pages("./tripadvisor.json")
        model = "trip_mainpage"
        page_config = None
        for webpage in webpages:
            for k, v in webpage.iteritems():
                if k == "model" and v == model:
                    page_config = webpage
        test_page = "http://www.tripadvisor.com.sg/Hotels-g294265-Singapore-Hotels.html"
        html = urllib2.urlopen(test_page).read()
        h = fromstring(html)
        for link in page_config["links"]:
            selector = CSSSelector(link["selector"])
            print link["selector"]
            els = selector(h)
            print len(els)
        pass
        #self.assertEqual(1, 1)
        #self.assertTrue(True)
   

if __name__ == '__main__':
    # Test all
    unittest.main()

