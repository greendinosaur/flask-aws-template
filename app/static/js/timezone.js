// ensures the browser timezone is added to relevant forms and URLs on the page
// this helps the server detect the user's timezone
// it is dependent on the moment.js file being loaded

'use strict';

if (window.attachEvent) {
    window.attachEvent('onload', add_tz_to_fields);
} else {
    if (window.onload) {
        const curronload = window.onload;
        const newonload = function (evt) {
            curronload(evt);
            add_tz_to_fields();
        };
        window.onload = newonload;
    } else {
        window.onload = add_tz_to_fields;
    }
}

// adds the browser timezone to the different fields in the web-page
function add_tz_to_fields() {
    add_user_tz();
    add_user_tz_to_form();
    format_exercise_date();
}

// adds the timezone to all of the elements that represent regular exercises
// these are identified by the presence of a css style on the lement
function add_user_tz() {
    const tz = moment.tz.guess();
    const elements = document.querySelectorAll('.stretched-link');

    for (let i = 0; i < elements.length; i++) {
        elements[i].href = elements[i].href + '?tz=' + tz;
    }
}

// adds the timezone to the hidden field in the form
// this form is used to enter a one-off exercise
function add_user_tz_to_form() {
    const tz = moment.tz.guess();
    const field = document.getElementById("user_tz");

    if (typeof (field) != 'undefined' && field != null) {
        field.value = tz;
    }
}

// formats the exercise date in the form field
// this is the form used to enter a one-off exercise
function format_exercise_date() {
    const field = document.getElementById("timestamp");

    if (typeof (field) != 'undefined' && field != null) {
        const m_utc = moment.utc(field.value, "DD/MM/YYYY HH:mm");
        const m_local = m_utc.clone().local().format("DD/MM/YYYY HH:mm");
        field.value = m_local;
    }
}
