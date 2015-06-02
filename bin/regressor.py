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
def createTestCaseJson(testCaseObject, testResult, currentImage, oldImage, differenceImage):
	testcase = {}
	testcase["name"] = testCaseObject.name
	testcase["url"] = testCaseObject.url
	testcase["height"] = testCaseObject.height
	testcase["width"] = testCaseObject.width

	if testResult.status is "0":
		testcase["success"] = True
	elif testResult.status is "unfinished": 
		testcase["success"] = "unfinished"
	else:
		global hadFailingTests
		hadFailingTests = True
		testcase["success"] = False

	testcase["message"] = testResult.message

	testcase["currentImage"] =  currentImage
	testcase["oldImage"] = oldImage
	testcase["differenceImage"] = differenceImage
	return testcase

def renameFile(fromName, toName):
	subprocess.call(["mv", fromName, toName])

def buildScreenshotFileName(screenshotDir, testCaseObject, postfix):
	return screenshotDir + testCaseObject.name + "_" + str(testCaseObject.height) + "_" +  str(testCaseObject.width) + postfix;

# main
if __name__ == '__main__':

	if len (sys.argv) < 3:
		print ('Usage: python regressor <screenshotDir> <json_file>')
	else:
		screenshotDir = sys.argv[1]
		json_file = sys.argv[2]
		testCases = parseSitesFromJson(json_file)
		
		completedTestCasesJson = []
		for testCaseObject in testCases:
			
			message = ""
			screenshotToTest = buildScreenshotFileName(screenshotDir, testCaseObject, postfixForTest)
			createScreenshot(testCaseObject, screenshotToTest)
			if os.path.isfile(screenshotToTest):
				currentImage = buildScreenshotFileName(screenshotDir, testCaseObject, postfixForCurrent)
				differenceImage = buildScreenshotFileName(screenshotDir, testCaseObject, postfixForDiff)
				oldImage= buildScreenshotFileName(screenshotDir, testCaseObject, postfixForOld)
				result = "unfinished"
				if os.path.isfile(currentImage):
					result = compareImages(screenshotToTest, currentImage, differenceImage)
					renameFile(currentImage, oldImage)	
				else:
					print("Could not find reference image for " + testCaseObject.name)
					message = "Could not find reference image for " + testCaseObject.name
				renameFile(screenshotToTest, currentImage)
			else:
				print("Unable to take screenshot")
				message = "Unable to take screenshot for " + testCaseObject.name
				hadFailingTests = True
				currentImage = ""
				differenceImage = ""
				oldImage = ""
				result = "failed"

			testResult = TestResult(result, message)
			completedTestCaseJson = createTestCaseJson(testCaseObject, testResult, currentImage, oldImage, differenceImage)
			completedTestCasesJson.append(completedTestCaseJson)	

		renderTemplate(completedTestCasesJson)		

		if hadFailingTests == False:
			sys.exit(0)
	
	sys.exit(1)
