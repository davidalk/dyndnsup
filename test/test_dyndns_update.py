'''
Created on 27 Dec 2013

@author: davidal-kanani
'''
import unittest
from dyndnsup import dyndns_update
from dyndnsup.dyndns_update import DynDnsInteract
from dyndnsup.dyndns_update import InvalidLoginError
from urllib import error

class TestDynDnsUpdate(unittest.TestCase):

    def testUnreachableUrl(self):
        interact = DynDnsInteract('http://www.url.bad', 'username', 
                                  'password', 'my.dn.com', '/usr/local/bin/phantomjs')
        with self.assertRaises(error.URLError):
            interact.login()
    
    def testValidLogin(self):
        (validuser, validpasswd, config) = dyndns_update.load_settings()
        interact = DynDnsInteract(config['DynDnsUrl'], validuser, 
                                  validpasswd, config['Hostname'], config['PhantomJS'])
        interact.login()
        self.assertEqual(interact.browser.title, 'My Dyn Account')
        
    def testInvalidLogin(self):
        interact = DynDnsInteract('https://account.dyn.com/entrance/', 'bad', 
                                  'login', 'my.dn.com', '/usr/local/bin/phantomjs')
        with self.assertRaises(InvalidLoginError):
            interact.login()
            
    def testMail(self):
        config = dyndns_update.load_settings()[2]
        ex = dyndns_update.InvalidLoginError('Test Exception')
        dyndns_update.send_error(ex, config)

if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()