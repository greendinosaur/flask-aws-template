'use strict';

const cookieName = "siteConsent";


function getCookieDomain() {
    return "; path=/; domain=" + document.location.hostname;
}

function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        let date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + getCookieDomain();
}

function getCookie(name) {
    let nameEQ = name + "=";
    let ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

function acceptCookie() {
    setCookie(cookieName, '1', '180');
    hideBanner();

}

function deleteCookie() {
    document.cookie = cookieName + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT' + getCookieDomain();
}

function hideBanner() {
    document.getElementById('cookie_banner').classList.add('d-none');
}

function showBanner() {
    document.getElementById('cookie_banner').classList.remove('d-none')
}

function cookieConsent() {
    if (!getCookie(cookieName)) {
        // show the cookie banner
        document.getElementById('cookie_accept').onclick = acceptCookie;
        showBanner();
    } else {
        hideBanner();

    }
}

window.onload = function () {
    cookieConsent();
};