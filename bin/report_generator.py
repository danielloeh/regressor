#! /usr/bin/python
from mako.template import Template
from datetime import datetime
from constants import TEMPLATE_FILE
from constants import RESULTING_HTML_FILE

def renderTemplate(testcases):

	positiveTests = 0
	negativeTests = 0
	unfinishedTests = 0

	for testcase in testcases:
		if testcase["success"] == True:
			positiveTests += 1
		elif testcase["success"] == False:
			negativeTests += 1
		else:
			unfinishedTests += 1

	mytemplate = Template(filename=TEMPLATE_FILE)
	result_string = mytemplate.render(testcases = testcases, 
			time = str(datetime.now()), 
			positiveTests = positiveTests, 
			negativeTests = negativeTests,
			unfinishedTests = unfinishedTests)
	writeHtmlFile(result_string)
		

def writeHtmlFile(htmlCode):
	result_html_file = open(RESULTING_HTML_FILE, "w")
	result_html_file.write(htmlCode)
	result_html_file.close()	