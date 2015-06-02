#! /usr/bin/python
import unittest
from Screenshots import *
from TestCase import TestCase

class ScreenshotsTest(unittest.TestCase):

	def testBuildScreenshotFileName(self):
		#given
		screenshotDir = "screenshots/"
		testcase =  TestCase("testcaseName", "url", "11", "12", 3000)
		postfix = "_postfix.jpg"

		#when
		filename = Screenshots.buildScreenshotFileName(testcase, postfix, screenshotDir)
		#then
		self.assertEqual(filename, "screenshots/testcaseName_11_12_postfix.jpg")


if __name__ == '__main__':
	unittest.main()