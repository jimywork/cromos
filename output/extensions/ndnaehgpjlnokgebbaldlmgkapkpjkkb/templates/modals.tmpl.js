this["Handlebars"] = this["Handlebars"] || {};
this["Handlebars"]["templates"] = this["Handlebars"]["templates"] || {};

this["Handlebars"]["templates"]["mtModalActivation.tmpl"] = Handlebars.template({"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var helper, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing, alias3="function", alias4=container.escapeExpression;

  return "<div class=\"tw-bs mt-modal mt-modal-activation\">   \n    <div class=\"modal\" tabindex=\"-1\" role=\"dialog\">\n        <div class=\"modal-dialog\">\n            <div class=\"modal-content text-center\">\n                <div class=\"modal-header\">\n                    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\">\n                        <span aria-hidden=\"true\">&times;</span>\n                    </button>\n                    <span class=\"mt-sprite mt-logo-icon\"></span>\n                    <h4 class=\"modal-title\">"
    + alias4(((helper = (helper = helpers.text || (depth0 != null ? depth0.text : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"text","hash":{},"data":data}) : helper)))
    + ": <strong>"
    + alias4(((helper = (helper = helpers.email || (depth0 != null ? depth0.email : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"email","hash":{},"data":data}) : helper)))
    + "</strong></h4>\n                </div>\n                <div class=\"modal-body\">\n                    <div class=\"activate-body\">\n                        <p class=\"big-cta\">\n                            <a href=\""
    + alias4(((helper = (helper = helpers.activateUrl || (depth0 != null ? depth0.activateUrl : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"activateUrl","hash":{},"data":data}) : helper)))
    + "\" target=\"_blank\" class=\"btn btn-primary btn-lg mt-modal-activation-activate mt-ga-event\" data-mt-ga-category=\"Activation-Popup\" data-mt-ga-action=\"Activate\">"
    + alias4(((helper = (helper = helpers.activate || (depth0 != null ? depth0.activate : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"activate","hash":{},"data":data}) : helper)))
    + "</a>\n                        </p>\n                        <p class=\"small\">"
    + alias4(((helper = (helper = helpers.disclaimer || (depth0 != null ? depth0.disclaimer : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"disclaimer","hash":{},"data":data}) : helper)))
    + "\n                            <a target=\"_blank\" class=\"terms mt-ga-event\" data-mt-ga-category=\"Activation-Popup\" data-mt-ga-action=\"See Terms\" href=\""
    + alias4(((helper = (helper = helpers.termsUrl || (depth0 != null ? depth0.termsUrl : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"termsUrl","hash":{},"data":data}) : helper)))
    + "\">"
    + alias4(((helper = (helper = helpers.terms || (depth0 != null ? depth0.terms : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"terms","hash":{},"data":data}) : helper)))
    + "</a>.</p>\n                    </div>\n                </div>\n                <div class=\"modal-footer\">\n                    <div class=\"btn-toolbar\">\n                        <a href=\"#\" data-dismiss=\"modal\" aria-label=\""
    + alias4(((helper = (helper = helpers.remindMeLater || (depth0 != null ? depth0.remindMeLater : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"remindMeLater","hash":{},"data":data}) : helper)))
    + "\" class=\"btn btn-sm mt-modal-activation-remind-me-later mt-ga-event\" data-mt-ga-category=\"Activation-Popup\" data-mt-ga-action=\"RemindLater\">"
    + alias4(((helper = (helper = helpers.remindMeLater || (depth0 != null ? depth0.remindMeLater : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"remindMeLater","hash":{},"data":data}) : helper)))
    + "</a>\n\n                        <a href=\"#\" data-dismiss=\"modal\" aria-label=\""
    + alias4(((helper = (helper = helpers.doNotUse || (depth0 != null ? depth0.doNotUse : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"doNotUse","hash":{},"data":data}) : helper)))
    + "\" class=\"btn btn-sm mt-modal-activation-do-not-use mt-ga-event\" data-mt-ga-category=\"Activation-Popup\" data-mt-ga-action=\"Disable\">"
    + alias4(((helper = (helper = helpers.doNotUse || (depth0 != null ? depth0.doNotUse : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"doNotUse","hash":{},"data":data}) : helper)))
    + "</a>\n                    </div>\n                </div>\n            </div>\n            <!-- /.modal-content -->\n        </div>\n        <!-- /.modal-dialog -->\n    </div>\n    <!-- /.modal -->\n</div>\n";
},"useData":true});

this["Handlebars"]["templates"]["mtModalFallback.tmpl"] = Handlebars.template({"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var stack1, helper, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing, alias3="function";

  return "<div class=\"tw-bs mt-modal mt-modal-fallback\">\n    <div class=\"modal\" tabindex=\"-1\" role=\"dialog\">\n        <div class=\"modal-dialog\">\n            <div class=\"modal-content\">\n                <div class=\"modal-header\">\n                    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\">\n                        <span aria-hidden=\"true\">&times;</span>\n                    </button>\n                    <span class=\"mt-sprite mt-logo-icon\"></span>\n                    <h4 class=\"modal-title\">"
    + container.escapeExpression(((helper = (helper = helpers.fallbackTitle || (depth0 != null ? depth0.fallbackTitle : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"fallbackTitle","hash":{},"data":data}) : helper)))
    + "</h4>\n                </div>\n                <div class=\"modal-body\">\n                    <p>"
    + ((stack1 = ((helper = (helper = helpers.fallbackText || (depth0 != null ? depth0.fallbackText : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"fallbackText","hash":{},"data":data}) : helper))) != null ? stack1 : "")
    + "</p>\n                </div>\n                <div class=\"modal-footer\"></div>\n            </div>\n            <!-- /.modal-content -->\n        </div>\n        <!-- /.modal-dialog -->\n    </div>\n    <!-- /.modal -->\n</div>\n";
},"useData":true});

this["Handlebars"]["templates"]["mtModalIframe.tmpl"] = Handlebars.template({"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var helper, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing, alias3="function", alias4=container.escapeExpression;

  return "<div class=\"tw-bs mt-modal mt-modal-iframe\">\n    <div class=\"modal\" tabindex=\"-1\" role=\"dialog\">\n        <div class=\"modal-dialog\">\n            <div class=\"modal-content\">\n                <div class=\"modal-header\">\n                    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\">\n                        <span aria-hidden=\"true\">&times;</span>\n                    </button>\n                </div>\n                <div class=\"modal-body\">\n                    <iframe frameBorder=\"0\" width=\""
    + alias4(((helper = (helper = helpers.width || (depth0 != null ? depth0.width : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"width","hash":{},"data":data}) : helper)))
    + "\" height=\""
    + alias4(((helper = (helper = helpers.height || (depth0 != null ? depth0.height : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"height","hash":{},"data":data}) : helper)))
    + "\" src=\""
    + alias4(((helper = (helper = helpers.src || (depth0 != null ? depth0.src : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"src","hash":{},"data":data}) : helper)))
    + "\"></iframe>\n                </div>\n                <div class=\"modal-footer\"></div>\n            </div>\n            <!-- /.modal-content -->\n        </div>\n        <!-- /.modal-dialog -->\n    </div>\n    <!-- /.modal -->\n</div>\n";
},"useData":true});

this["Handlebars"]["templates"]["mtModalIncompatibleExtension.tmpl"] = Handlebars.template({"1":function(container,depth0,helpers,partials,data) {
    return "                                    <li>"
    + container.escapeExpression(container.lambda(depth0, depth0))
    + "</li>\n";
},"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var stack1, helper, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing, alias3="function", alias4=container.escapeExpression;

  return "<div class=\"tw-bs mt-modal mt-modal-incompatible-extension\">\n    <div class=\"modal\" tabindex=\"-1\" role=\"dialog\">\n        <div class=\"modal-dialog\">\n            <div class=\"modal-content\">\n                <div class=\"modal-header text-center\">\n                    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\">\n                        <span aria-hidden=\"true\">&times;</span>\n                    </button>\n                    <span class=\"mt-sprite mt-logo-icon\"></span>\n                    <h4 class=\"modal-title\">"
    + alias4(((helper = (helper = helpers.title || (depth0 != null ? depth0.title : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"title","hash":{},"data":data}) : helper)))
    + "</h4>\n                </div>\n                <div class=\"modal-body\">\n                    <div class=\"text-center\">\n                      <p>"
    + ((stack1 = ((helper = (helper = helpers.explanation || (depth0 != null ? depth0.explanation : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"explanation","hash":{},"data":data}) : helper))) != null ? stack1 : "")
    + "</p>\n                    </div>\n                    <div class=\"panel panel-info\">\n                      <div class=\"panel-heading\">\n                        <h3 class=\"panel-title\">Instructions</h3>\n                      </div>\n                      <div class=\"panel-body\">\n                        <ol class=\"steps\">\n                            <li>\n                                <h4>"
    + alias4(((helper = (helper = helpers.step1Title || (depth0 != null ? depth0.step1Title : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"step1Title","hash":{},"data":data}) : helper)))
    + "</h4>\n                                <h5>"
    + alias4(((helper = (helper = helpers.step1ListTitle || (depth0 != null ? depth0.step1ListTitle : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"step1ListTitle","hash":{},"data":data}) : helper)))
    + "</h5>\n                                <ul>\n"
    + ((stack1 = helpers.each.call(alias1,(depth0 != null ? depth0.extensions : depth0),{"name":"each","hash":{},"fn":container.program(1, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "                                </ul>\n                                <p>\n                                  <a\n                                      href=\"chrome://extensions\"\n                                      aria-label=\""
    + alias4(((helper = (helper = helpers.step1CallToAction || (depth0 != null ? depth0.step1CallToAction : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"step1CallToAction","hash":{},"data":data}) : helper)))
    + "\"\n                                      target=\"_blank\"\n                                      class=\"btn btn-primary btn-sm  mt-modal-incompatible-extension-open-chrome-extensions mt-ga-event\"\n                                      data-mt-ga-category=\"Incompatible-Extension-Popup\"\n                                      data-mt-ga-action=\"Go to Extensions settings\">"
    + alias4(((helper = (helper = helpers.step1CallToAction || (depth0 != null ? depth0.step1CallToAction : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"step1CallToAction","hash":{},"data":data}) : helper)))
    + "</a>\n                                </p>\n                            </li>\n                            <li>\n                                <h4>"
    + alias4(((helper = (helper = helpers.step2Title || (depth0 != null ? depth0.step2Title : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"step2Title","hash":{},"data":data}) : helper)))
    + "</h4>\n                                <p>\n                                  <a href=\"#\" aria-label=\""
    + alias4(((helper = (helper = helpers.step2CallToAction || (depth0 != null ? depth0.step2CallToAction : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"step2CallToAction","hash":{},"data":data}) : helper)))
    + "\" class=\"btn btn-primary btn-sm  mt-modal-incompatible-extension-refresh-gmail mt-ga-event\" data-mt-ga-category=\"Incompatible-Extension-Popup\" data-mt-ga-action=\"Refresh Gmail\">"
    + alias4(((helper = (helper = helpers.step2CallToAction || (depth0 != null ? depth0.step2CallToAction : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"step2CallToAction","hash":{},"data":data}) : helper)))
    + "</a>\n                                </p>\n                            </li>\n                        </ol>\n                      </div>\n                    </div>\n                </div>\n                <div class=\"modal-footer\">\n                    <p class=\"do-not-show\">\n                        <a href=\"#\" data-dismiss=\"modal\" aria-label=\""
    + alias4(((helper = (helper = helpers.doNotUse || (depth0 != null ? depth0.doNotUse : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"doNotUse","hash":{},"data":data}) : helper)))
    + "\" class=\"dismiss-link mt-modal-incompatible-extension-disable mt-ga-event\" data-mt-ga-category=\"Incompatible-Extension-Popup\" data-mt-ga-action=\"Do not show me again\">"
    + alias4(((helper = (helper = helpers.doNotShow || (depth0 != null ? depth0.doNotShow : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"doNotShow","hash":{},"data":data}) : helper)))
    + "</a>\n                    </p>\n                </div>\n            </div>\n            <!-- /.modal-content -->\n        </div>\n        <!-- /.modal-dialog -->\n    </div>\n    <!-- /.modal -->\n</div>\n";
},"useData":true});

this["Handlebars"]["templates"]["mtModalIncompatibleLabs.tmpl"] = Handlebars.template({"1":function(container,depth0,helpers,partials,data) {
    return "                                    <li>"
    + container.escapeExpression(container.lambda(depth0, depth0))
    + "</li>\n";
},"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var stack1, helper, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing, alias3="function", alias4=container.escapeExpression;

  return "<div class=\"tw-bs mt-modal mt-modal-incompatible-labs\">\n    <div class=\"modal\" tabindex=\"-1\" role=\"dialog\">\n        <div class=\"modal-dialog\">\n            <div class=\"modal-content\">\n                <div class=\"modal-header text-center\">\n                    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\">\n                        <span aria-hidden=\"true\">&times;</span>\n                    </button>\n                    <span class=\"mt-sprite mt-logo-icon\"></span>\n                    <h4 class=\"modal-title\">"
    + alias4(((helper = (helper = helpers.title || (depth0 != null ? depth0.title : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"title","hash":{},"data":data}) : helper)))
    + "</h4>\n                </div>\n                <div class=\"modal-body\">\n                    <div class=\"text-center\">\n                      <p>"
    + ((stack1 = ((helper = (helper = helpers.explanation || (depth0 != null ? depth0.explanation : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"explanation","hash":{},"data":data}) : helper))) != null ? stack1 : "")
    + "</p>\n                    </div>\n\n\n                    <div class=\"panel panel-info\">\n                      <div class=\"panel-heading\">\n                        <h3 class=\"panel-title\">Instructions</h3>\n                      </div>\n                      <div class=\"panel-body\">\n                        <ol class=\"steps\">\n                            <li>\n                                <h4>"
    + alias4(((helper = (helper = helpers.step1Title || (depth0 != null ? depth0.step1Title : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"step1Title","hash":{},"data":data}) : helper)))
    + "</h4>\n                                <h5>"
    + alias4(((helper = (helper = helpers.step1ListTitle || (depth0 != null ? depth0.step1ListTitle : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"step1ListTitle","hash":{},"data":data}) : helper)))
    + "</h5>\n                                <ul>\n"
    + ((stack1 = helpers.each.call(alias1,(depth0 != null ? depth0.labs : depth0),{"name":"each","hash":{},"fn":container.program(1, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "                                </ul>\n                                <p>\n                                  <a href=\"https://mail.google.com/mail/#settings/general\" aria-label=\""
    + alias4(((helper = (helper = helpers.step1CallToAction || (depth0 != null ? depth0.step1CallToAction : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"step1CallToAction","hash":{},"data":data}) : helper)))
    + "\" target=\"_blank\" class=\"btn btn-primary mt-ga-event\" data-mt-ga-category=\"Incompatible-Labs-Popup\" data-mt-ga-action=\"Go to Extensions settings\">"
    + alias4(((helper = (helper = helpers.step1CallToAction || (depth0 != null ? depth0.step1CallToAction : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"step1CallToAction","hash":{},"data":data}) : helper)))
    + "</a>\n                                </p>\n                            </li>\n                        </ol>\n                      </div>\n                    </div>\n\n                </div>\n                <div class=\"modal-footer\">\n                    <p class=\"do-not-show\">\n                        <a href=\"#\" data-dismiss=\"modal\" aria-label=\""
    + alias4(((helper = (helper = helpers.doNotUse || (depth0 != null ? depth0.doNotUse : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"doNotUse","hash":{},"data":data}) : helper)))
    + "\" class=\"dismiss-link mt-modal-incompatible-labs-disable mt-ga-event\" data-mt-ga-category=\"Incompatible-Labs-Popup\" data-mt-ga-action=\"Do not show me again\">"
    + alias4(((helper = (helper = helpers.doNotShow || (depth0 != null ? depth0.doNotShow : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"doNotShow","hash":{},"data":data}) : helper)))
    + "</a>\n                    </p>\n                </div>\n            </div>\n            <!-- /.modal-content -->\n        </div>\n        <!-- /.modal-dialog -->\n    </div>\n    <!-- /.modal -->\n</div>\n";
},"useData":true});

this["Handlebars"]["templates"]["mtModalTitleBodyButton.tmpl"] = Handlebars.template({"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var stack1, helper, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing, alias3="function", alias4=container.escapeExpression;

  return "<div class=\"tw-bs mt-modal mt-modal-title-body-button\">\n    <div class=\"modal\" tabindex=\"-1\" role=\"dialog\">\n        <div class=\"modal-dialog\">\n            <div class=\"modal-content text-center\">\n                <div class=\"modal-header\">\n                    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\">\n                        <span aria-hidden=\"true\">&times;</span>\n                    </button>\n                    <span class=\"mt-sprite mt-logo-icon\"></span>\n                    <h4 class=\"modal-title\">"
    + alias4(((helper = (helper = helpers.title || (depth0 != null ? depth0.title : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"title","hash":{},"data":data}) : helper)))
    + "</h4>\n                </div>\n                <div class=\"modal-body\">\n                    <p>"
    + ((stack1 = ((helper = (helper = helpers.body || (depth0 != null ? depth0.body : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"body","hash":{},"data":data}) : helper))) != null ? stack1 : "")
    + "</p>\n                </div>\n                <div class=\"modal-footer\">\n                    <button type=\"button\" data-dismiss=\"modal\" aria-label=\""
    + alias4(((helper = (helper = helpers.button || (depth0 != null ? depth0.button : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"button","hash":{},"data":data}) : helper)))
    + "\" class=\"btn btn-primary mt-button\" data-dismiss=\"modal\">"
    + alias4(((helper = (helper = helpers.button || (depth0 != null ? depth0.button : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"button","hash":{},"data":data}) : helper)))
    + "</button>\n                </div>\n            </div>\n            <!-- /.modal-content -->\n        </div>\n        <!-- /.modal-dialog -->\n    </div>\n    <!-- /.modal -->\n</div>\n";
},"useData":true});

this["Handlebars"]["templates"]["mtModalTitleBodyButtonLink.tmpl"] = Handlebars.template({"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var stack1, helper, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing, alias3="function", alias4=container.escapeExpression;

  return "<div class=\"tw-bs mt-modal mt-modal-title-body-button-link\">\n    <div class=\"modal\" tabindex=\"-1\" role=\"dialog\">\n        <div class=\"modal-dialog\">\n            <div class=\"modal-content text-center\">\n                <div class=\"modal-header\">\n                    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\">\n                        <span aria-hidden=\"true\">&times;</span>\n                    </button>\n                    <span class=\"mt-sprite mt-logo-icon\"></span>\n                    <h4 class=\"modal-title\">"
    + alias4(((helper = (helper = helpers.title || (depth0 != null ? depth0.title : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"title","hash":{},"data":data}) : helper)))
    + "</h4>\n                </div>\n                <div class=\"modal-body\">\n                    <p>"
    + ((stack1 = ((helper = (helper = helpers.body || (depth0 != null ? depth0.body : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"body","hash":{},"data":data}) : helper))) != null ? stack1 : "")
    + "</p>\n                </div>\n                <div class=\"modal-footer\">\n                    <button type=\"button\" data-dismiss=\"modal\" aria-label=\""
    + alias4(((helper = (helper = helpers.button || (depth0 != null ? depth0.button : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"button","hash":{},"data":data}) : helper)))
    + "\" class=\"btn btn-primary mt-button\">"
    + alias4(((helper = (helper = helpers.button || (depth0 != null ? depth0.button : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"button","hash":{},"data":data}) : helper)))
    + "</button>\n                    <a href=\"#\" data-dismiss=\"modal\" aria-label=\""
    + alias4(((helper = (helper = helpers.link || (depth0 != null ? depth0.link : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"link","hash":{},"data":data}) : helper)))
    + "\" class=\"mt-link dismiss-link\">"
    + alias4(((helper = (helper = helpers.link || (depth0 != null ? depth0.link : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"link","hash":{},"data":data}) : helper)))
    + "</a>\n                </div>\n            </div>\n            <!-- /.modal-content -->\n        </div>\n        <!-- /.modal-dialog -->\n    </div>\n    <!-- /.modal -->\n</div>\n";
},"useData":true});
