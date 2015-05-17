#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import subprocess
import os.path
from siteparser import parseSitesFromJson
from constants import *
from report_generator import renderTemplate
from screenshot_comparer import *

################################
# This little script uses phantomjs and compare (imagemagick)
# to compare a previous version of a website with the current state, based on screenshots (aka regression test)
# All testcases (urls + viewport settings) have to be configured in a file named sites.json 
# {
#   "testcase" : <testcasename>,
#	"url" : <url>,
#	"width" : <viewportwidth>,
#	"height" : <viewportheight>,
# 	"waitAfterDomCompleteInMs" :<time in ms to wait to make screenshot after DOM is ready>
# }
# Author: Daniel Löffelholz
#
# Open features
# - configuration of different view ports for each site
# - add render time to result
###############################

#variables
hadFailingTests = False

# functions
def createTestCase(testcaseName, testcaseUrl, testcaseHeight, testcaseWidth, currentImage, oldImage, differenceImage, result):
	testcase = {}
	testcase["name"] = testcaseName
	if result is "0":
		testcase["success"] = True
	elif result is "uncompleted": 
		testcase["success"] = "uncompleted"
	else:
		global hadFailingTests
		hadFailingTests = True
		testcase["success"] = False
	testcase["url"] = testcaseUrl
	testcase["height"] = testcaseHeight
	testcase["width"] = testcaseWidth
	testcase["currentImage"] =  currentImage
	testcase["oldImage"] = oldImage
	testcase["differenceImage"] = differenceImage
	return testcase

def renameFile(fromName, toName):
	subprocess.call(["mv", fromName, toName])


# main
if __name__ == '__main__':

	if len (sys.argv) < 2:
		print ('Usage: python html_templating <screenshotDir>')
	else:
		sites_map = parseSitesFromJson(JSON_FILE)
		screenshotDir = sys.argv[1]
		testcases = []
		for site_entry in sites_map:
			testcaseName = site_entry["testcase"]
			testcaseUrl = site_entry["url"]
			testcaseHeight = site_entry["height"]
			testcaseWidth = site_entry["width"]
			waitForMsAfterDomReady = site_entry["waitAfterDomCompleteInMs"]
		
			screenshotToTest = screenshotDir + testcaseName + postfixForTest;
						
			createScreenshot(testcaseUrl, testcaseHeight, testcaseWidth, screenshotToTest, waitForMsAfterDomReady)

			currentImage = screenshotDir + testcaseName + postfixForCurrent
			differenceImage = screenshotDir + testcaseName + postfixForDiff
			oldImage= screenshotDir + testcaseName + postfixForOld
			result = "uncompleted"
			if os.path.isfile(currentImage):
				result = compareImages(screenshotToTest, currentImage, differenceImage)
				renameFile(currentImage, oldImage)	
			else:
				print("Could not find reference image for " + testcaseName)
			testcase = createTestCase(testcaseName, testcaseUrl, testcaseHeight, testcaseWidth, currentImage, oldImage, differenceImage, result)
			testcases.append(testcase)	
			renameFile(screenshotToTest, currentImage)

	renderTemplate(testcases)		

	if hadFailingTests == True:
		sys.exit(0)
	else:
		sys.exit(1)
