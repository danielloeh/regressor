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
			<a href="#${testcase['name']}">
				<img class="jump_icon" src="icons/appbar.control.play.png" /><p class="jump_text">${testcase['name']}</p>
			</a>
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
	<hr />
	<div class="testcase">
		<a name="${testcase['name']}"></a>
		<div class="testcase_indicator  ${selectTestCaseResult(testcase)}">&nbsp;</div>
		<h2>${testcase['name']} : <a href="${testcase['url']}" target="_blank">${testcase['url']}</a> (height: ${testcase['height']}/width: ${testcase['width']})</h2>
		% if testcase['message'] != "":
			<div class="message_box">
				<img style="float:left" src="icons/appbar.transit.hazard.png" />
				<p class="message_text">${testcase['message']} </p>
			</div>	
		% endif
		<div class="jump_container">
			% if testcase['currentImage'] != "":
			<div class="jump_box">
				<a target="_blank" href="${testcase['currentImage']}">
					<img class="jump_icon" src="icons/appbar.door.enter.png" /><p class="jump_text">current</p>
				</a>
			</div>
			% endif
			% if testcase['oldImage'] != "":
			<div class="jump_box">
				<a target="_blank" href="${testcase['oldImage']}">
					<img class="jump_icon" src="icons/appbar.door.enter.png" /><p class="jump_text">old</p>
				</a>
			</div>
			% endif
			% if testcase['differenceImage'] != "":
			<div class="jump_box">
				<a target="_blank" href="${testcase['differenceImage']}">
					<img class="jump_icon" src="icons/appbar.door.enter.png" /><p class="jump_text">difference</p>
				</a>
			</div>
			% endif
		</div>
		% if testcase['currentImage'] != "":
		<p>
			<img 
				class="testcaseImage" 
				src="${testcase['currentImage']}"
				% if testcase['success'] != 'unfinished':
					onmouseover="this.src='${testcase['differenceImage']}';"
					onmouseout="this.src='${testcase['currentImage']}';" 
				% endif
				/>
		</p>
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