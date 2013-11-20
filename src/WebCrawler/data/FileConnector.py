#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Save data into file
# require happybase

import os
import happybase


class FileConnector(object):
    """ Maintain the connection with hbase database. 
        Perform put operation on database.
    """

    def __init__ (self, root):
        """ Init the connector with root dir. 
        """
        self.root = root 
        self.table = None

    def connect_table(self, table):
        """ Connect to the specified table in hbase.
        """
        self.table = os.path.join(self.root, table)

    def check_table(self, table):
        """ Check if the table is available.
        """
        tables = [d for d in os.listdir(self.root) \
                  if os.path.isdir(os.path.join(self.root, d))]
        if table not in tables:
            return False
        return True
    
    def initialize_table(self, table):
        """ Initialize table.
        """
        os.mkdir(os.path.join(self.root, table))    
        return self.check_table(table)

    def save_data(self, data, table, pks=["id"]):
        """ Save review data into hbase. 
        """
        pkdata = []
        for pk in pks:
            if pk not in data.keys():
                return False
            pkdata.append(str(data[pk])) 
        row_key = "-".join(pkdata) 
        row_key = row_key.replace('/', '_')
        filename = os.path.join(self.root, table, row_key+'.txt')
        with open(filename, 'w') as f:
            for key in data.keys():
                if key not in pks:
                    column = "%s" % key
                    f.write("%s:%s\n" % (column, data[key]))
        return True

    
if __name__ == "__main__":
    pass
