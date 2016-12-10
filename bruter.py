#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Brute SubDomain
  Created: 2016/12/7
"""

import unittest
import json 
from os import system
from threading import Thread
from time import sleep
from pprint import pprint

from guesser import check_existed
from dict_parser import DictParser
from thread_pool import Pool



########################################################################
class Bruter(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, target, dict_file, thread_max, 
                 timeout=5, nameservers=[]):
        """Constructor"""
        assert isinstance(target, (str, unicode))
        self.target = target
        
        self._timeout = timeout
        self._nameservers = nameservers
        
        self._absolutely_no_such_domain_ = 'a-b-s-o-l-u-t-e-l-y-n-o'
        self.first_error_domain = '.'.join([self._absolutely_no_such_domain_, self.target])

        self.error_ip_or_empty = check_existed(subdomain=self.first_error_domain,
                                               nameserver=self._nameservers,
                                               timeout=timeout)['IP']
        self._dict_parser = DictParser(dict_file)
        
        self._thread_max = thread_max
        
        self._pool = Pool(self._thread_max)
        self._pool.start()
        
    #----------------------------------------------------------------------
    def _start(self):
        """"""

        while self._dict_parser.finished == False:
            subdomain_pre = self._dict_parser.next()
            
            if self._pool.get_current_task_queue_len() <= 10:
                #print subdomain_pre
                _target = '.'.join([subdomain_pre, self.target])
                self._pool.feed(check_existed, _target)
            else:
                sleep(0.3)
    
    #----------------------------------------------------------------------
    def start(self):
        """"""
        ret = Thread(target=self._start)
        #ret.daemon = True
        ret.start()
        
        result_queue = self._pool.get_result_queue()
        while True:
            try:
                #print 'Waiting for result'
                #print result_queue.qsize()
                ret = result_queue.get(timeout=3)
                self._parse_result(ret)
            except:
                pass
            
    #----------------------------------------------------------------------
    def _parse_result(self, result):
        """"""
        if result['state']:
            if result['result']['state']:
                _IP = result['result']['IP']
                _target = result['result']['target']
                if _IP == self.error_ip_or_empty:
                    pass
                else:
                    self._process_result({'target':_target,
                                          'ip':_IP})
        else:
            pass
        
    #----------------------------------------------------------------------
    def _process_result(self, r):
        """"""
        pprint(r)
        system('echo "%s" >> %s.txt' % (json.dumps(r), self.target))
        
        
        



########################################################################
class BruterTest(unittest.case.TestCase):
    """"""

    #----------------------------------------------------------------------
    def runTest(self):
        """Constructor"""
        
        btr = Bruter('uestc.edu.cn', './dict/subnames.txt', thread_max=30)
        result_queue = btr.start()

    
    
        
        
if __name__ == '__main__':
    unittest.main()