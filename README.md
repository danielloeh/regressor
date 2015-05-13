# regressor
This little tool compare a previous version of a website with the current state, based on screenshots (aka regression testing)
An html report will be  generated in the working directory which displays the screenshots and differences 
All testcases have to be configured in a file named 'sites.json' (see file for examples)

Author: Daniel Löffelholz daniel.loeffelholz@gmail.com

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

Known Issues:
 
