/* El código a continuación es propiedad intelectual de The Mail Track Company S.L. de Barcelona, España,
y solo debe ser utilizado y manejado bajo estos Términos: https://mailtrack.io/es/terms

The code hereafter is the intellectual property of The Mail Track Company S.L. of Barcelona, Spain
and must be used and handled only according to these Terms: https://mailtrack.io/en/terms */
/* El código a continuación es propiedad intelectual de The Mail Track Company S.L. de Barcelona y es secreto industrial.

The code hereafter is the intellectual property of The Mail Track Company S.L. of Barcelona, Spain and is a Trade Secret. */

(function () {
    'use strict';

    var intercom = document.createElement('script');

    intercom.textContent = '(function(){var w=window; w.MT_INTERCOM_PATH="' + chrome.runtime.getURL('').slice(0, -1) + '/scripts/lib/' + '";var ic=w.Intercom;if(typeof ic==="function"){ic("reattach_activator");ic("update",intercomSettings);}else{var d=document;var i=function(){i.c(arguments)};i.q=[];i.c=function(args){i.q.push(args)};w.Intercom=i;function l(){var s=d.createElement("script");s.type="text/javascript";s.async=true;s.src=w.MT_INTERCOM_PATH + "intercom-shim.js";var x=d.getElementsByTagName("script")[0];x.parentNode.insertBefore(s,x);}if(w.attachEvent){w.attachEvent("onload",l);}else{w.addEventListener("load",l,false);}}})()'; // https://docs.intercom.com/install-on-your-product-or-site/other-ways-to-get-started/integrate-intercom-in-a-single-page-app

    document.documentElement.appendChild(intercom);
}());
