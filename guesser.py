#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Check A domain existed
  Created: 2016/12/7
"""

import unittest
from pprint import pprint
from dns import resolver
from dns.exception import Timeout

#----------------------------------------------------------------------
def check_existed(subdomain, nameserver=[], timeout=5, ):
    """"""
    result = {}
    result['state'] = False
    result['IP'] = ''
    result['target'] = subdomain
    
    checker = resolver.Resolver()
    if isinstance(nameserver, (list, tuple)):
        if nameserver == []:
            pass
        else:
            for _ in nameserver:
                assert isinstance(_, (str, unicode)) , \
                       '[!] TypeError! should be a str/unicode'
                
            checker.nameservers = nameserver
    else:
        assert isinstance(nameserver, (str, unicode)), \
            '[!] add_nameserver should be a str/unicode or list/tuple'
        
        checker.nameservers.insert(0, _)
        
    assert isinstance(timeout, int)
    checker.lifetime = timeout
    
    try:
        answer = checker.query(subdomain)
        result['state'] = True
    except:
        result['state'] = False
    #pprint(result)
    if result['state']:
        for i in answer.response.answer:
            result['IP'] = i.to_text().split()[-1]
        return result
    else:
        return result
    


########################################################################
class CheckTest(unittest.case.TestCase):
    """"""

    #----------------------------------------------------------------------
    def runTest(self):
        """Constructor"""
        s = check_existed('sa.villanch.top')
        pprint(s)
        self.assertTrue(s.has_key('state'))

if __name__ == '__main__':
    unittest.main()