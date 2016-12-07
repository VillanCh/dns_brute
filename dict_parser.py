#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Parser Dict
  Created: 2016/12/7
"""

import unittest
import time

########################################################################
class DictParser(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, dict_file):
        """Constructor"""
        self.dict_file = dict_file
        
        self.dict_file_pf = None
        
        self.count = 0
        self.dict_file_pf = open(dict_file)
    
        self.finished = False
    
    #----------------------------------------------------------------------
    def __del__(self):
        """"""
        self.dict_file_pf.close()
    
    #----------------------------------------------------------------------
    def next(self):
        """"""
        self.count + 1
        self.empty = 0
        if self.finished:
            return False
        else:
            pass
        
        while True:
            _ = self.dict_file_pf.readline().strip()
            if _ == '' or _ == u'':
                self.empty = self.empty + 1
                if self.empty > 100:
                    self.finished = True
                    break
                continue
            else:
                return _
        
        
########################################################################
class DictParserTest(unittest.case.TestCase):
    """"""

    #----------------------------------------------------------------------
    def runTest(self):
        """Constructor"""
        dp = DictParser(dict_file='LICENSE')
        while True:
            _ = dp.next()
            if _ == False:
                break
            else:
                print _
        
        print('TEST SUCCESS')
        
    
    
if __name__ == '__main__':
    unittest.main()