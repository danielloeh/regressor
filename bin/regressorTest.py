#! /usr/bin/python
import unittest
from regressor import createTestCaseJson
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


if __name__ == '__main__':
	unittest.main()