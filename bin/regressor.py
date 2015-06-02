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
from Screenshots import *

################################
# This little script uses phantomjs and compare (imagemagick)
# to compare a previous version of a website with the current state, based on screenshots (aka regression test)
# All testcases (urls + viewport settings) have to be configured in a file named sites.json 
# 
# Author: Daniel Löffelholz, daniel.loeffelholz@gmail.com
# Company: Silpion IT-Solutions GmbH
#
# github: https://github.com/danielloeh/regressor
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

def iterateOverTestCasesMakeScreenshotComparisonAndCreateTestCaseResultJson(screenshotDir, testCases):
	testCaseJsonList = []
	for testCaseObject in testCases:		
		message = ""
		screenshots = Screenshots(testCaseObject, screenshotDir)
		createScreenshot(testCaseObject, screenshots.testName())
		if os.path.isfile(screenshots.testName()):	
			result = "unfinished"
			if os.path.isfile(screenshots.currentName()):
				result = compareImages(screenshots.testName(), screenshots.currentName(), screenshots.diffName())
				renameFile(screenshots.currentName(), screenshots.oldName())	
			else:
				message = "Could not find reference image for " + testCaseObject.name
			renameFile(screenshots.testName(), screenshots.currentName())
			completedTestCaseJson = createTestCaseJson(testCaseObject, TestResult(result, message), screenshots.currentName(),  screenshots.oldName(),  
				screenshots.diffName())
			testCaseJsonList.append(completedTestCaseJson)

		else:
			message = "Unable to take screenshot for " + testCaseObject.name
			global hadFailingTests
			hadFailingTests = True
			completedTestCaseJson = createTestCaseJson(testCaseObject, TestResult("failed", message), "", "", "")
			testCaseJsonList.append(completedTestCaseJson)

		if(message is not ""):
			print(message)
				
	return testCaseJsonList

# main
if __name__ == '__main__':

	if len (sys.argv) < 3:
		print ('Usage: python regressor <screenshotDir> <json_file>')
	else:
		screenshotDir = sys.argv[1]
		json_file = sys.argv[2]
		testCases = parseSitesFromJson(json_file)
		
		testCaseJsonList = iterateOverTestCasesMakeScreenshotComparisonAndCreateTestCaseResultJson(screenshotDir, testCases)

		renderTemplate(testCaseJsonList)		

		if hadFailingTests == False:
			sys.exit(0)
	
	sys.exit(1)
