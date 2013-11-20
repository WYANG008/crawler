#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unit Test for Webcrawler.parser 

@author Wang Qiang
"""

import unittest
import urllib2
from WebCrawler.config import config
from WebCrawler.parser import parser


class UnitTest(unittest.TestCase):
    """
    test for Webcrawler.parser.
    """
    @unittest.skip("Tested") 
    def testParser_trip_main(self):
        pages_config = config.load_pages("../config/tripadvisor.json")
        model = "trip_mainpage"
        page_config = None
        for webpage in pages_config:
            for k, v in webpage.iteritems():
                if k == "model" and v == model:
                    page_config = webpage

        test_page = "http://www.tripadvisor.com.sg/Hotels-g294265-Singapore-Hotels.html"
        html = urllib2.urlopen(test_page).read()
        data, links = parser.parse_page(html, page_config)
        print len(data)
        print len(links)
        self.assertEqual(len(data), 30)
        self.assertEqual(len(links), 32)
   
    @unittest.skip("Tested") 
    def testParser_trip_review(self):
        pages_config = config.load_pages("../config/tripadvisor.json")
        model = "trip_review"
        page_config = None
        for webpage in pages_config:
            for k, v in webpage.iteritems():
                if k == "model" and v == model:
                    page_config = webpage

        test_page = "http://www.tripadvisor.com.sg/Restaurant_Review-g294265-d2516429-Reviews-Auld_Alliance-Singapore.html"
        html = urllib2.urlopen(test_page).read()
        data, links = parser.parse_page(html, page_config)
        print links
        print len(data)
        print len(links)
   
    #@unittest.skip("Tested") 
    def testParser_trip_review_detail(self):
        pages_config = config.load_pages("../config/tripadvisor.json")
        model = "trip_review_detail"
        page_config = config.get_model_config(pages_config, model)

        test_page = "http://www.tripadvisor.com.sg/ShowUserReviews-g294265-d2516429-r165190313-Auld_Alliance-Singapore.html"
        test_page = "http://www.tripadvisor.com.sg/ShowUserReviews-g294265-d2516429-r139369230-Auld_Alliance-Singapore.html#REVIEWS"
        html = urllib2.urlopen(test_page).read()
        data, links = parser.parse_page(html, page_config)
        print data
        print links
        print len(data)
        print len(links)
   

    @unittest.skip("Tested") 
    def testParser_hungry_list(self):
        pages_config = config.load_pages("../config/hungrygowhere.json")
        model = "hungrygowhere_review_list"
        page_config = None
        for webpage in pages_config:
            for k, v in webpage.iteritems():
                if k == "model" and v == model:
                    page_config = webpage

        test_page = "http://www.hungrygowhere.com/reviews/"
        html = urllib2.urlopen(test_page).read()
        data, links = parser.parse_page(html, page_config)
        print links
        print len(data)
        print len(links)
   

    @unittest.skip("Tested") 
    def testParser_hungry_link(self):
        pages_config = config.load_pages("../config/hungrygowhere.json")
        model = "hungrygowhere_review_link"
        page_config = None
        for webpage in pages_config:
            for k, v in webpage.iteritems():
                if k == "model" and v == model:
                    page_config = webpage

        test_page = "http://www.hungrygowhere.com/singapore/je_crab_specialist_tampines/"
        html = urllib2.urlopen(test_page).read()
        data, links = parser.parse_page(html, page_config)
        print links
        print data
        print len(data)
        print len(links)


    @unittest.skip("Tested") 
    def testParser_hungry_detail(self):
        pages_config = config.load_pages("../config/hungrygowhere.json")
        model = "hungrygowhere_review_detail"
        page_config = None
        for webpage in pages_config:
            for k, v in webpage.iteritems():
                if k == "model" and v == model:
                    page_config = webpage

        test_page = "http://www.hungrygowhere.com/singapore/je_crab_specialist_tampines/review/id-1f340200/"
        html = urllib2.urlopen(test_page).read()
        data, links = parser.parse_page(html, page_config)
        print links
        print data
        print len(data)
        print len(links)


if __name__ == '__main__':
    # Test all
    unittest.main()

