#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright (c) 2013, Revolution Analytics
# All rights reserved.


""" Database Related Operation
"""

from WebCrawler import settings
from WebCrawler.data.HbaseConnector import HbaseConnector
from WebCrawler.data.FileConnector import FileConnector

if settings.database == "FILE":
    connector = FileConnector(settings.database_name)
elif settings.database == "HBASE":
    connector = HbaseConnector(settings.hbase_host, settings.hbase_port)

def check_table(table):
    """ Check if the table exist in the database.
    """
    return connector.check_table(table)

def initialize_table(table):
    """ Create the table in database.
    """
    return connector.initialize_table(table)

def save_data(data, table, webconfig):
    """ Save the data into database.
    """
    pks = []
    attributes = webconfig["attributes"]
    for attribute in attributes:
        if attribute['pk']:
            pks.append(attribute["name"])
    connector.save_data(data, table, pks)
    pass


if __name__ == "__main__":
    pass
