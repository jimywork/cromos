/* El código a continuación es propiedad intelectual de The Mail Track Company S.L. de Barcelona, España,
y solo debe ser utilizado y manejado bajo estos Términos: https://mailtrack.io/es/terms

The code hereafter is the intellectual property of The Mail Track Company S.L. of Barcelona, Spain
and must be used and handled only according to these Terms: https://mailtrack.io/en/terms */
(function (ElementProto) {
    if (typeof ElementProto.matches !== 'function') {
        ElementProto.matches = ElementProto.msMatchesSelector || ElementProto.mozMatchesSelector || ElementProto.webkitMatchesSelector || function matches (selector) {
            var element = this;
            var elements = (element.document || element.ownerDocument).querySelectorAll(selector);
            var index = 0;

            while (elements[index] && elements[index] !== element) {
                ++index;
            }

            return Boolean(elements[index]);
        };
    }

    if (typeof ElementProto.closest !== 'function') {
        ElementProto.closest = function closest (selector) {
            var element = this;

            while (element && element.nodeType === 1) {
                if (element.matches(selector)) {
                    return element;
                }

                element = element.parentNode;
            }

            return null;
        };
    }
})(window.Element.prototype);
