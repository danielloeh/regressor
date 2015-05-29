# Regressor v 0.1

 What? 
- Frontend rendering regression testing tool

Why?
- Increasing css complexity increases the need of tests
- Functional tests do not cover how it actually looks when it's rendered
- the more often you deploy, the more expensive your manual testing gets
- Its hard to find the little bugs by manual testing (like a slightly different font or a changing space between items)
- The more often you deploy, the more important the automated regression testing gets

How?
- It compares a previous version of a website with the current state, based on screenshots 
- An html report will be  generated which displays the testcases, their screenshots and differences to the previous version
- Different resolutions can be configured for each testcase to test multiple breakpoints (for responsive)
- Testcases are configured in sites.json

Author: Daniel Löffelholz daniel.loeffelholz@gmail.com
Company: Silpion IT-Solutions GmbH

Technology:
- python (including mako templating)
- javascript 
- imagemagick 
- phantomjs

Usage:
- optional : apt-get install phantomjs 
- optional : apt-get install imagemagick
- ./regression_test.sh

Open Features:
- Activly confirm a failed screenshot

 
