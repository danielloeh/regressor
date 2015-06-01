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
- Testcases are separately configured in a json file (see `sites.example.json`)

Author: Daniel Löffelholz daniel.loeffelholz@gmail.com

Company: Silpion IT-Solutions GmbH

Technology:
- python (including mako templating)
- javascript 
- imagemagick 
- phantomjs

Requirements:
- phantomjs (`apt-get install phantomjs`)
- imagemagick (`apt-get install imagemagick`)

Quickstart:
- Clone project
- Create your `sites.json` from `sites.example.json`
- run `run.sh sites.json`
- check results in `result.html`
- Best used in your build pipeline after deploying to a certain environment 
- Running unittests: `/bin/run_test.sh`

Recommended setup:

Variant 1:
- Use regressor as submodule in your local repository for versioning your local testfile (see
 https://github.com/danielloeh/regressor/wiki/How-to-integrate-into-your-local-Git-Repository)
- Based on that, use it on jenkins (see https://github.com/danielloeh/regressor/wiki/Integrate-on-jenkins-build-server-with-git-plugin)

Variant 2: 
- Just checkout the project
- Modify your testcase file locally on all your environments


