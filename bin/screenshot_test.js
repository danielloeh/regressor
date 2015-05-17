
var system = require('system');
var args = system.args;


if( args.length < 6 || args.length > 6){
	console.log("Usage: screenshot_test.js URL viewportWidth viewportHeight filename timeAfterDomReadyInMs")
	phantom.exit();
} else{
	var url = args[1]; 
	var viewPortWidth = args[2];
	var viewPortHeight = args[3];
	var screenshotName = args[4];
	var timeAfterDomReady = args[5]
	console.log("Accessing: " + url + " (" + viewPortWidth + "px /" + viewPortHeight + " px). Writing to file: "+ screenshotName);
	var page = require('webpage').create();
	t = Date.now();

	page.onInitialized = function (){
		page.onCallback = function(data) {
			
			t = Date.now()- t;
			console.log("Page loading time " + t + " msec");
			window.setTimeout(function(){
				page.render(screenshotName);
				console.log("Screenshot written");
				phantom.exit();		
				}, timeAfterDomReady); // offset for lazy loaded things
		};

		page.evaluate(function() {
			document.addEventListener("DOMContentLoaded", function(){
				window.callPhantom();
			}, false);
		});
	};


	page.viewportSize = { width: viewPortWidth,	height: viewPortHeight };

	page.open(url, function(status){
		if(status !== 'success'){
			console.log("Unable to load the address!");
		} else {
			/* checking for dom ready is only possible with callback on site (see above)*/
		}
 });
}


