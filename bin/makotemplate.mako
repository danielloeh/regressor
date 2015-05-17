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
			Summary: Total ${negativeTests + positiveTests} (Passing: ${positiveTests} / Failing: ${negativeTests})
		</div>

		% for testcase in testcases:
		<div class="quicklink %{selectTestCaseResult(testcase)}">
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
			<div class="testcase_indicator %{selectTestCaseResult(testcase)}">&nbsp;</div>
			<h2>${testcase['name']} : ${testcase['url']} (${testcase['height']}/${testcase['width']})</h2>
			<div>
			<a target="blank" href="${testcase['currentImage']}">current</a>
			<a target="blank" href="${testcase['oldImage']}">old</a>
			<a target="blank" href="${testcase['differenceImage']}">difference</a>
		</div>
			<img 
				class="testcaseImage" 
				src="${testcase['currentImage']}"
				% if testcase['success'] != 'uncompleted':
					onmouseover="this.src='${testcase['differenceImage']}';"
					onmouseout="this.src='${testcase['currentImage']}';" 
				% endif
				/>
		</div>
</%def>


<%def name="selectTestCaseresult(testcase)">
	% if testcase['success'] == True:
		testcase_success
	% elif testcase['success'] == 'uncompleted':
		testcase_incomplete
	% else:
 		testcase_failed
	% endif
</%def>