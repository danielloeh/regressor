#! /usr/bin/python
import unittest
from regressor import createTestCase
from TestResult import TestResult

class RegressorTest(unittest.TestCase):


	def testCreateSuccessfulTestCase(self):
		#given
		expectedTestCase = { "name" : "testcaseName",
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
		#when
		testcase =  createTestCase("testcaseName", "testcaseUrl", "testcaseHeight", "testcaseWidth",
		 	"currentImage", "oldImage", "differenceImage", testResult)
		
		#then
		self.assertEqual(testcase, expectedTestCase)


if __name__ == '__main__':
	unittest.main()