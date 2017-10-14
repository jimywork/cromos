/* El código a continuación es propiedad intelectual de The Mail Track Company S.L. de Barcelona y es secreto industrial.

The code hereafter is the intellectual property of The Mail Track Company S.L. of Barcelona, Spain and is a Trade Secret. */
(function () {
    'use strict';

  // TODO: this options should be in a external file.
    var options = [
        {
            name: 'settings',
            activate: true,
            caption: 'settingsOption_settings',
            href: 'https://mailtrack.io/reauth?url=https%3A%2F%2Fmailtrack.io%2Fapp_dev.php%2Fen%2Fdashboard%2Fsettings'
        },
        {
            name: 'account',
            activate: true,
            caption: 'settingsOption_account',
            href: 'https://mailtrack.io/reauth?url=https%3A%2F%2Fmailtrack.io%2Fapp_dev.php%2Fen%2Fdashboard%2Faccount'
        },
        {
            name: 'faqs',
            activate: true,
            caption: 'settingsOption_faqs',
            href: 'https://mailtrack.desk.com'
        },
        {
            name: 'dashboard',
            activate: true,
            caption: 'settingsOption_dashboard',
            href: 'https://mailtrack.io/reauth?url=https%3A%2F%2Fmailtrack.io%2Fapp_dev.php%2Fen%2Fdashboard%2F'
        },
        {
            name: 'upgrade',
            activate: true,
            caption: 'settingsOption_upgrade',
            href: 'https://mailtrack.io/reauth?url=https%3A%2F%2Fmailtrack.io%2Fapp_dev.php%2Fen%2Fdashboard%2Fpayment%3Futm_source=gmail%26utm_medium=menu%26utm_campaign=updatemenu'
        }
    ];

    var label, icon, link, item, list, wrapper;

  /**
   * creates a label for the option
   *
   * @return {span node}
   */
    function createLabel () {
        var label = document.createElement('span');
        label.classList.add('label');
        return label;
    }

  /**
   * creates a icon for the option
   *
   * @return {span node}
   */
    function createIcon () {
        var icon = document.createElement('span');
        icon.classList.add('icon');
        return icon;
    }

  /**
   * creates a link to a option
   *
   * @param  {span node} icon  icon of option
   * @param  {span node} label label of option
   *
   * @return {link node}
   */
    function createLink (icon, label) {
        var link = document.createElement('a');
        link.classList.add('link');
        link.setAttribute('target', '_blank');
        link.appendChild(icon);
        link.appendChild(label);
        return link;
    }

  /**
   * creates a option
   *
   * @param  {link node} link
   *
   * @return {list item node}
   */
    function createItem (link) {
        var item = document.createElement('li');
        item.appendChild(link);
        return item;
    }

  /**
   * creates a ul element
   *
   * @return {ul node}
   */
    function createList () {
        var list = document.createElement('ul');
        return list;
    }

  /**
   * Check if the option should be in the form.
   *
   * @param  {object}  option candidate to append to HTML form
   *
   * @return {Boolean}        true if should be shown on the form
   */
    function isActivate (option) {
        return option.activate;
    }

  /**
   * append option to form
   *
   * @param  {object}  option to append to HTML form
   */
    function addOption (option) {
        var itemCloned = item.cloneNode(true);
        var linkCloned = itemCloned.querySelector('a');
        var labelCloned = itemCloned.querySelector('.label');
        var iconCloned = itemCloned.querySelector('.icon');
        var caption = chrome.i18n.getMessage(option.caption) || option.caption;

        // eslint-disable-next-line no-unsafe-innerhtml/no-unsafe-innerhtml
        labelCloned.innerHTML = caption;
        iconCloned.classList.add(option.name);
        linkCloned.setAttribute('href', option.href);

        list.appendChild(itemCloned);
    }

  /**
   * append the valid options on HTML form
   *
   * @param  {ul node} list    HTML Element to append the new options
   * @param  {array} options description of options to append
   */
    function createOptions (options) {
        label = createLabel();
        icon = createIcon();
        link = createLink(icon, label);
        item = createItem(link);
        list = createList();

        wrapper = document.querySelector('.mt-mailtrack-extension-button .wrapper');
        wrapper.appendChild(list);

        options
      .filter(isActivate)
      .forEach(addOption);
    }

    if (window.navigator.userAgent.toLowerCase().includes('edge')) {
        const script = document.createElement('script');

        // eslint-disable-next-line scanjs-rules/assign_to_src
        script.src = '/scripts/lib/backgroundScriptsAPIBridge.js';
        script.async = false;
        script.onload = () => {
            createOptions(options);
        };
        document.head.appendChild(script);
    } else {
        createOptions(options);
    }
})();
