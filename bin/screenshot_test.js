
var system = require('system');
var args = system.args;


if( args.length < 6 || args.length > 6){
	console.log("Usage: screenshot_test.js URL viewportHeight viewportWidth filename timeAfterDomReadyInMs")
	phantom.exit();
} else{
	var url = args[1]; 
	var viewPortHeight = args[2];
	var viewPortWidth = args[3];
	var screenshotName = args[4];
	var timeAfterDomReady = args[5]
	console.log("Accessing: " + url + " (h:" + viewPortHeight + "px /w:" + viewPortWidth + " px). Writing to file: "+ screenshotName);
	var page = require('webpage').create();
	t = Date.now();


	page.onResourceError = function(resourceError){
		page.reason = resourceError.errorString;
		page.reason_url = resourceError.url;
	}

	page.onInitialized = function (){
		page.onCallback = function(data) {
			t = Date.now()- t;
			console.log("Page loading time " + t + " msec");
			window.setTimeout(function(){
				page.render(screenshotName);
				console.log("Screenshot written");
				phantom.exit(0);		
				}, timeAfterDomReady); // offset for lazy loaded things
		};

		page.evaluate(function() {
			document.addEventListener("DOMContentLoaded", function(){
				window.callPhantom();
			}, false);
		});
	};


	page.viewportSize = { width: viewPortWidth,	height: viewPortHeight };
	try {
		page.open(url, function(status){
			if(status !== 'success'){
				   console.log("Error opening url \"" + page.reason_url + "\": " + page.reason);
	            phantom.exit(1);
			} else {
				/* checking for dom ready is only possible with callback on site (see above)*/
			}
	 	});
	} finally{
		setTimeout(function(){
			console.log("Max execution time " + Math.round(10000) + " seconds exceeded");
			phantom.exit(1);
		}, 10000);
	}
}


