'''
Created on 27 Dec 2013

@author: davidal-kanani
'''

from selenium import webdriver
import requests
import configparser
import os

def main():
    pass

def load_settings():
    config = configparser.ConfigParser()
    file = os.path.join(os.path.dirname(__file__), 'settings.cfg')
    config.read_file(open(file))
    username = config['USER']['username']
    password = config['USER']['password']
    return (username, password, config['CONFIG'])

class DynDnsInteract:
    
    phantomjs_bin = '/usr/local/bin/phantomjs'
    
    def __init__(self, url, notify_email, username, passwd, hostname):
        self.url = url
        self.notify_email = notify_email
        self.username = username
        self.passwd = passwd
        self.hostname = hostname
        self.browser = None
        
        
    def login(self):
        # Use requests module to check valid url as
        # selenium webdriver doesn't have this function!
        r = requests.get(self.url)
        r.raise_for_status()
         
        self.browser = webdriver.PhantomJS(DynDnsInteract.phantomjs_bin)
        self.browser.get(self.url)
        self.browser.implicitly_wait(10)
         
        username = self.browser.find_element_by_name('username')
        password = self.browser.find_element_by_name('password')
        submit = self.browser.find_element_by_name('submit')
         
        username.send_keys(self.username)
        password.send_keys(self.passwd)        
        submit.click()
        if self.browser.title != 'My Dyn Account':
            raise InvalidLoginException('Login failed, browser title: ' + self.browser.title)
        print('Login to DynDns Successful')
        
        
    def update_ip(self, ip_addr):
        myhosts = self.browser.find_element_by_link_text('My Hosts')
        myhosts.click()
        hostname = self.browser.find_element_by_link_text(self.hostname)
        hostname.click()
        cur_ip = self.browser.find_element_by_name('cur_ip')
        print('Current ip is: ' + cur_ip.get_attribute('value'))
        if cur_ip.get_attribute('value') != ip_addr:
            cur_ip.clear()
            cur_ip.send_keys(ip_addr)
            print('Update ip to:' + ip_addr)
        save = self.browser.find_element_by_name('submit')
        save.click()


class InvalidLoginException(Exception):
    def __init__(self, message):
        self.message = message

if __name__ == '__main__':
    main()