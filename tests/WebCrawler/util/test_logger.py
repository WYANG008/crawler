#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unit Test for util.logger 

@author Wang Qiang
"""
import unittest
from WebCrawler.util.logger import setup_logger

class TestLogger(unittest.TestCase):
    def test_logger(self):
        logger = setup_logger("Tester")
        cl = logger.debug
        cl("Logger Test")
        self.assertTrue(True)
        pass

if __name__ == "__main__":
    unittest.main()
