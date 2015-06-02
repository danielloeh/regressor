#! /usr/bin/python
import unittest
from regressor import createTestCaseJson
from regressor import buildScreenshotFileName
from TestResult import TestResult
from TestCase import TestCase

class RegressorTest(unittest.TestCase):


	def testCreateSuccessfulTestCaseJson(self):
		#given
		expectedTestCaseJson = { "name" : "testcaseName",
								"url" : "testcaseUrl",
								"height" : "testcaseHeight",
								"width" : "testcaseWidth",
								"currentImage" : "currentImage",
								"oldImage" : "oldImage",
								"differenceImage" : "differenceImage",	
								"success" : True,
								"message" : "good"
							}
		testResult = TestResult("0","good")
		testCaseObject = TestCase("testcaseName", "testcaseUrl", "testcaseHeight", "testcaseWidth", 42)

		#when
		testcaseJson=  createTestCaseJson(testCaseObject, testResult, "currentImage", "oldImage", "differenceImage")
		
		#then
		self.assertEqual(testcaseJson, expectedTestCaseJson)

	def testBuildScreenshotFileName(self):
		#given
		screenshotDir = "screenshots/"
		testcase =  TestCase("testcaseName", "url", "11", "12", 3000)
		postfix = "_postfix.jpg"

		#when
		filename = buildScreenshotFileName(screenshotDir, testcase, postfix)
		#then
		self.assertEqual(filename, "screenshots/testcaseName_11_12_postfix.jpg")


if __name__ == '__main__':
	unittest.main()