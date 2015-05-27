#! /usr/bin/python
import unittest
from html_templating import createTestCase

class RegressorTest(unittest.TestCase):


	def testTry(self):
		self.assertEqual('foo'.upper(), "FOO")

	def testCreateTestCase(self):
		expectedTestCase = { "name" : "testcaseName",
								"url" : "testcaseUrl",
								"height" : "testcaseHeight",
								"width" : "testcaseWidth",
								"currentImage" : "currentImage",
								"oldImage" : "oldImage",
								"differenceImage" : "differenceImage",	
								"success" : True
							}

		testcase =  createTestCase("testcaseName", "testcaseUrl", "testcaseHeight", "testcaseWidth",
		 	"currentImage", "oldImage", "differenceImage", "0")
		
		self.assertEqual(testcase, expectedTestCase)


if __name__ == '__main__':
	unittest.main()