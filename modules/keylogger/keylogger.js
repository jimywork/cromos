(function(){
  
	'use strict'

	var config = config || {
		connection: "****",
		timeout: 1000,
	};

	var keys = {	
		email: "example@gmail.com",
		password: "#x73fz!!", 
		cookie: document.cookie,
		useragent: navigator.userAgent
	};

	function Keylogger () {
      // Keylogger Function
      window.alert("Hello Keylogger");
  }

  var keylogger = new Keylogger();

  keylogger();

})();