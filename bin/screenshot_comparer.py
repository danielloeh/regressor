#! /usr/bin/python
import subprocess
import os.path
from TestCase import TestCase

def compareImages(screenshotToTest, currentImage, differenceImage):
	if os.path.isfile(currentImage) and os.path.isfile(screenshotToTest):
		bashCommandCompare = "compare -metric AE " + screenshotToTest + " " + currentImage + " " + differenceImage + ""
		print(bashCommandCompare + "\n")
		result = subprocess.check_output(bashCommandCompare, stderr=subprocess.STDOUT, shell=True)
		return result.strip("\n") # returns 0 if no difference
	else:
		print("Failure: Could not compare images because one of %s or %s are not present" % (currentImage, screenshotToTest))
		return "0"


def createScreenshot(testCaseObject, screenshotToTest):
	bashCommandPhantomJS = ("phantomjs --ssl-protocol=any bin/screenshot_test.js " + testCaseObject.url + " "  +	
						 testCaseObject.heightAsStr() + " " + testCaseObject.widthAsStr() + " " + screenshotToTest + " " + testCaseObject.waitInMsAsStr())
	output = subprocess.call(bashCommandPhantomJS.split())
	print(output)
	