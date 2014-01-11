'''
Created on 27 Dec 2013

@author: davidal-kanani
'''

from selenium import webdriver
from urllib import request
import configparser
import os
import re

def main():
    (username, password, config) = load_settings()
    interact = DynDnsInteract(config['DynDnsUrl'], config['Email'], username, 
                              password, config['Hostname'], config['PhantomJS'])
    interact.login()
    external_ip = get_external_ip(config['PhantomJS'])
    interact.update_ip(external_ip)
    

def load_settings():
    config = configparser.ConfigParser()
    file = os.path.join(os.path.dirname(__file__), 'settings.cfg')
    config.read_file(open(file))
    username = config['USER']['username']
    password = config['USER']['password']
    return (username, password, config['CONFIG'])

def get_external_ip(phantomjs_bin):
        browser = webdriver.PhantomJS(phantomjs_bin)
        browser.implicitly_wait(10)
        browser.get('http://checkip.dyndns.org')
        body = browser.find_element_by_tag_name('body')
        ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", body.text)[0]
        return ip
        

class DynDnsInteract:
    
    
    def __init__(self, dyndnsurl, notify_email, username, passwd, hostname, phantomjs_bin):
        self.dyndnsurl = dyndnsurl
        self.notify_email = notify_email
        self.username = username
        self.passwd = passwd
        self.hostname = hostname
        self.phantomjs_bin = phantomjs_bin
        self.browser = None
        
        
    def login(self):
        request.urlopen(self.dyndnsurl)
         
        self.browser = webdriver.PhantomJS(self.phantomjs_bin)
        self.browser.get(self.dyndnsurl)
        self.browser.implicitly_wait(10)
         
        username = self.browser.find_element_by_name('username')
        password = self.browser.find_element_by_name('password')
        submit = self.browser.find_element_by_name('submit')
         
        username.send_keys(self.username)
        password.send_keys(self.passwd)        
        submit.click()
        if self.browser.title != 'My Dyn Account':
            raise InvalidLoginError('Login failed, browser title: ' + self.browser.title)
        print('Login to DynDns Successful')
        
        
    def update_ip(self, external_ip):
        myhosts = self.browser.find_element_by_link_text('My Hosts')
        myhosts.click()
        hostname = self.browser.find_element_by_link_text(self.hostname)
        hostname.click()
        cur_ip = self.browser.find_element_by_name('cur_ip')
        
        print('Current DynDns ip is: ' + cur_ip.get_attribute('value'))
        
        if cur_ip.get_attribute('value') != external_ip:
            cur_ip.clear()
            cur_ip.send_keys(external_ip)
            print('Update ip to: ' + external_ip)
        else:
            print('Ip up to date, not updating')
            
        save = self.browser.find_element_by_name('submit')
        save.click()


class InvalidLoginError(Exception):
    pass

if __name__ == '__main__':
    main()