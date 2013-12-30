# dyndnsup
==============

Automatic refresh of dyndns service, minimum Python version 3.3 required


Setup:

1. Install [PhantomJS](http://phantomjs.org/download.html)

2. Ues your prefered Python package manager to install [Selenium](https://pypi.python.org/pypi/selenium)

3. Download this repository

4. Create a file called settings.cfg in the same directory as the dyndns_update.py module file, sample file as follows:

```
[USER]
Username = youruser
Password = yourpass

[CONFIG]
DynDnsUrl = https://account.dyn.com/entrance/
Hostname = yourhost.dyndns-free.com
Email = your@mail.com
PhantomJS = /usr/local/bin/phantomjs
```