
async function loadScript(url) {
    let response = await fetch(url);
    let script = await response.text();
    eval(script);
  }
  
  let scriptUrl = 'https://code.jquery.com/jquery-3.6.0.min.js'
  loadScript(scriptUrl);

chrome.extension.sendMessage({}, function (response) {
	var readyStateCheckInterval = setInterval(function () {
		if (document.readyState === "complete") {
            let scriptUrl = 'https://code.jquery.com/jquery-3.6.0.min.js'
            loadScript(scriptUrl);
			clearInterval(readyStateCheckInterval);

			// ----------------------------------------------------------
			// This part of the script triggers when page is done loading
			console.log("Hello. This message was sent from scripts/inject.js");
			// ----------------------------------------------------------
			setInterval(clickConnect, 60000);	//1 minute
			//setInterval(clickConnect, 20000);	//20 sec
		}
	}, 10);
});



// Credit to https://medium.com/@shivamrawat_756/how-to-prevent-google-colab-from-disconnecting-717b88a128c0
function clickConnect() {
	try {
		 document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect").click();
		// this also works, if above one doesn't work, comment it and uncomment below one
		//document.querySelector("colab-connect-button").shadowRoot.getElementById('connect').click();
		setTimeout(clickDismiss, 2000);
		console.log("Keeping Colab Alive!");	
	} catch (error) {
		console.log(error);
	}
}

function clickDismiss() {
	try {
		document.querySelector('colab-sessions-dialog').shadowRoot.querySelector('.dismiss').click();
		console.log('clicked on dismiss button');
	} catch (error) {
		console.log(error);
	}
}

jQuery("div > colab-run-button").click()
jQuery("#ok").click()