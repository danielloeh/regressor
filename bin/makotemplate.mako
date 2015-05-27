<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Results for regression test</title>
		<link rel="stylesheet" href="report.css" type="text/css" />
	</head>
	<body>
		<h1>Regression Test Suite (${time})</h1>

		<div>
			Summary: Total ${negativeTests + positiveTests} (Passing: ${positiveTests} / Failing: ${negativeTests} / Unfinished: ${unfinishedTests})
		</div>

		% for testcase in testcases:
		<div class="quicklink ${selectTestCaseResult(testcase)}">
			<a href="#${testcase['name']}">${testcase['name']}</a>
		</div> 
		% endfor
			
		<div class="testcasebox">
		% for testcase in testcases:
			${buildTestCase(testcase)}
		% endfor
		</div>
	</body>
</html>



<%def name="buildTestCase(testcase)">
	<div class="testcase">
		<a name="${testcase['name']}"></a>
		<div class="testcase_indicator  ${selectTestCaseResult(testcase)}">&nbsp;</div>
		<h2>${testcase['name']} : <a href="${testcase['url']}" target="_blank">${testcase['url']}</a> (height: ${testcase['height']}/width: ${testcase['width']})</h2>
		% if testcase['message'] != "":
			<p>Message: ${testcase['message']}</p>	
		% endif
		<div>
			% if testcase['currentImage'] != "":
			<a target="_blank" href="${testcase['currentImage']}">current</a>
			% endif
			% if testcase['oldImage'] != "":
			<a target="_blank" href="${testcase['oldImage']}">old</a>
			% endif
			% if testcase['differenceImage'] != "":
			<a target="_blank" href="${testcase['differenceImage']}">difference</a>
			% endif
		</div>
		% if testcase['currentImage'] != "":
		<img 
			class="testcaseImage" 
			src="${testcase['currentImage']}"
			% if testcase['success'] != 'unfinished':
				onmouseover="this.src='${testcase['differenceImage']}';"
				onmouseout="this.src='${testcase['currentImage']}';" 
			% endif
			/>
		% endif
	</div>
</%def>


<%def name="selectTestCaseResult(testcase)">
	% if testcase['success'] == True:
		testcase_success
	% elif testcase['success'] == 'unfinished':
		testcase_incomplete
	% else:
 		testcase_failed
	% endif
</%def>