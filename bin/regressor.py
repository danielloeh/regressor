	#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import subprocess
import os.path
from siteparser import parseSitesFromJson
from constants import *
from report_generator import renderTemplate
from screenshot_comparer import *
from TestResult import TestResult
from TestCase import TestCase

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
# - delete reference images with wrong dimensions
###############################

#variables
hadFailingTests = False

# functions
def createTestCase(testcaseName, testcaseUrl, testcaseHeight, testcaseWidth, currentImage, oldImage, differenceImage, testResult):
	testcase = {}
	testcase["name"] = testcaseName
	result = testResult.status
	message = testResult.message
	if result is "0":
		testcase["success"] = True
	elif result is "unfinished": 
		testcase["success"] = "unfinished"
	else:
		global hadFailingTests
		hadFailingTests = True
		testcase["success"] = False
	testcase["message"] = message
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
		testCases = parseSitesFromJson(JSON_FILE)
		screenshotDir = sys.argv[1]
		completedTestCases = []
		for testCase in testCases:
			
			message = ""
			screenshotToTest = screenshotDir + testCase.name + "_" + str(testCase.height) + "_" +  str(testCase.width) + postfixForTest;
			createScreenshot(testCase.url, testCase.height, testCase.width, screenshotToTest, testCase.waitInMs)
			if os.path.isfile(screenshotToTest):
				currentImage = screenshotDir + testCase.name + "_" + str(testCase.height) + "_" +  str(testCase.width) + postfixForCurrent
				differenceImage = screenshotDir + testCase.name + "_" + str(testCase.height) + "_" +  str(testCase.width) + postfixForDiff
				oldImage= screenshotDir + testCase.name  + "_" + str(testCase.height) + "_" +  str(testCase.width) + postfixForOld
				result = "unfinished"
				if os.path.isfile(currentImage):
					result = compareImages(screenshotToTest, currentImage, differenceImage)
					renameFile(currentImage, oldImage)	
				else:
					print("Could not find reference image for " + testCase.name)
					message = "Could not find reference image for " + testCase.name
				renameFile(screenshotToTest, currentImage)
			else:
				print("Unable to take screenshot")
				message = "Unable to take screenshot for " + testCase.name
				hadFailingTests = True
				currentImage = ""
				differenceImage = ""
				oldImage = ""
				result = "failed"

			testResult = TestResult(result, message)
			completedTestCase = createTestCase(testCase.name, testCase.url, testCase.height, testCase.width, currentImage, oldImage, differenceImage, testResult)
			completedTestCases.append(completedTestCase)	

	renderTemplate(completedTestCases)		

	if hadFailingTests == True:
		sys.exit(1)
	else:
		sys.exit(0)
