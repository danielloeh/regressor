#! /usr/bin/python
import unittest
from TestCase import TestCase
from siteparser import testCasesAlreadyContainTestCaseName

class SiteParserTest(unittest.TestCase):


	def testShouldReturnTrueIfTestCaseNameIsAlreadyContained(self):
		# given
		testcases = []
		testCaseName = "someTestCase"
		someOtherTestCase = TestCase("someTestCase", "unusedUrl", "42", "42", "42")
		testcases.append(someOtherTestCase)

		# when

		alreadyContainsTestCaseName = testCasesAlreadyContainTestCaseName(testCaseName, testcases)

		# then
		self.assertTrue(alreadyContainsTestCaseName)

	def testShouldReturnFalseIfTestCaseNameIsNotContained(self):
		# given
		testcases = []
		testCaseName = "someTestCase"
		someOtherTestCase = TestCase("someOtherTestCaseName", "unusedUrl", "42", "42", "42")
		testcases.append(someOtherTestCase)

		# when

		alreadyContainsTestCaseName = testCasesAlreadyContainTestCaseName(testCaseName, testcases)

		# then
		self.assertFalse(alreadyContainsTestCaseName)
	

if __name__ == '__main__':
	unittest.main()