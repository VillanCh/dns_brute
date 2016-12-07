#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Brute SubDomain
  Created: 2016/12/7
"""

import unittest
from guesser import check_existed


########################################################################
class Bruter(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, target):
        """Constructor"""
        assert isinstance(target, (str, unicode))
        self.target = target
        
        self._absolutely_no_such_domain_ = 'a-b-s-o-l-u-t-e-l-y-n-o'
        self.first_error_domain = '.'.join([self._absolutely_no_such_domain_, self.target])

        self.error_ip_or_empty = check_existed(subdomain=self.first_error_domain)['IP']
        
        
    #----------------------------------------------------------------------
    def start(self):
        """"""
        
        
        
if __name__ == '__main__':
    unittest.main()