#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Hbase connection
# require happybase

import happybase


class HbaseConnector(object):
    """ Maintain the connection with hbase database. 
        Perform put operation on database.
    """

    def __init__ (self, host='localhost', port=9090):
        """ Init the connector with host name and port.
            The default host is 'localhost', the default port is 9090.
        """
        self.host = host
        self.port = port
        self.table = None

    def connect_table(self, table):
        """ Connect to the specified table in hbase.
        """
        connection = happybase.Connection(self.host, self.port)
        self.table = connection.table(table)

    def check_table(self, table):
        """ Check if the table is available.
        """
        connection = happybase.Connection(self.host, self.port)
        tables = connection.tables()
        if table not in tables:
            return False
        return True
    
    def initialize_table(self, table):
        """ Initialize table.
        """
        connection = happybase.Connection(self.host, self.port)
        connection.create_table(
            table,
            {
                'data' : dict(), 
            }
        )
        return self.check_table(table)

    def save_data(self, data, table, pks=["id"]):
        """ Save review data into hbase. 
        """
        connection = happybase.Connection(self.host, self.port)
        self.table = connection.table(table)
        pkdata = []
        for pk in pks:
            if pk not in data.keys():
                return False
            pkdata.append(str(data[pk])) 
        row_key = "-".join(pkdata) 
        for key in data.keys():
            if key not in pks:
                column = "data:%s" % key
                self.table.put(row_key, {column : data[key]})
        return True

    
if __name__ == "__main__":
    connector = HbaseConnector()
    print connector.check_table("test")
    pass
