#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unit Test for WebCrawler.job task_manager 

@author Wang Qiang
"""

import unittest
from WebCrawler.job import task_manager


class UnitTest(unittest.TestCase):
    """
    test for WebCrawler.job task_manager 
    """
    
    def testTaskManager(self):
        task_manager.start("../config/")
        self.assertTrue(True)
   

if __name__ == '__main__':
    # Test all
    unittest.main()
