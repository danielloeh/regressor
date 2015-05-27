#! /usr/bin/python
import json
from TestCase import TestCase

def parseSitesFromJson(jsonFile):
	with open(jsonFile) as json_file:
		data = json.load(json_file)

		testcases = []

		for site_entry in data:
			testCaseName = site_entry["testcase"]
			testcaseUrl = site_entry["url"]
			testcaseHeight = site_entry["height"]
			testcaseWidth = site_entry["width"]
			waitForMsAfterDomReady = site_entry["waitAfterDomCompleteInMs"]

			testcase = TestCase(testCaseName, testcaseUrl, testcaseHeight, testcaseWidth, waitForMsAfterDomReady)
			if not testCasesAlreadyContainTestCaseName(testCaseName, testcases):
				testcases.append(testcase)
			else:
				print("[WARNING] Ignored testcase "+ testCaseName + " because name was already used.")
		return testcases


def testCasesAlreadyContainTestCaseName(testCaseName, testCases):
	for testCase in testCases:
		if testCase.name == testCaseName:
			return True
	return False






