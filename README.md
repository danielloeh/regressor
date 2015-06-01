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
- It will exit with 0 or 1, depending in the testresult so it can be used as part of a build pipeline
- An html report will be generated which displays the testcases, their screenshots and differences to the previous version
- Different resolutions can be configured for each testcase to test multiple breakpoints (for responsive)
- Testcases are separately configured in a json file (see sites.example.json)

Author: Daniel Löffelholz daniel.loeffelholz@gmail.com
Company: Silpion IT-Solutions GmbH

Technology:
- python (including mako templating)
- javascript 
- imagemagick 
- phantomjs

Requirements:
- phantomjs (apt-get install phantomjs)
- imagemagick apt-get install imagemagick

Quickstart:
- Clone project
- Create your `sites.json` from `sites.example.json`
- run `run.sh sites.json`
- Best used in your build pipeline after deploying to a certain environment (for setup recommendations read: https://github.com/danielloeh/regressor/wiki/How-to-integrate-into-your-local-Git-Repository
- Running unittests: `/bin/run_test.sh`


