from constants import *

class Screenshots(object):

	def __init__(self, testCaseObject, screenshotDir):
		self.screenshotDir = screenshotDir
		self.testCaseObject = testCaseObject
		
	def currentName(self):
		return Screenshots.buildScreenshotFileName(self.testCaseObject, postfixForCurrent, self.screenshotDir)

	def testName(self):
		return Screenshots.buildScreenshotFileName(self.testCaseObject, postfixForTest, self.screenshotDir)

	def diffName(self):
		return Screenshots.buildScreenshotFileName(self.testCaseObject, postfixForDiff, self.screenshotDir)

	def oldName(self):
		return Screenshots.buildScreenshotFileName(self.testCaseObject, postfixForOld, self.screenshotDir)

	@staticmethod
	def buildScreenshotFileName(testCaseObject, postfix, screenshotDir):
		return screenshotDir + testCaseObject.name + "_" + str(testCaseObject.height) + "_" +  str(testCaseObject.width) + postfix;
