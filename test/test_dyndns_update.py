'''
Created on 27 Dec 2013

@author: davidal-kanani
'''
import unittest
from dyndnsup.dyndns_update import DynDnsInteract
from requests import RequestException

class TestDynDnsUpdate(unittest.TestCase):


    def testInvalidUrl(self):
        interact = DynDnsInteract('www.url.bad', 'test@mail.com', 'username', 'password')
        with self.assertRaises(RequestException):
            interact.login()
    
    @unittest.skip("not ready yet") 
    def testValidLogin(self):
        interact = DynDnsInteract('https://account.dyn.com/entrance/', 'david.alkanani@gmail.com', 'davidalk', 'da5624')
        interact.login()
        self.assertEqual(interact.browser.current_url, 'My Dyn Account')


if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()