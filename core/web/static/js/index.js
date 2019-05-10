console.log('loaded');

$(document).ready(function() {
    // Connect to the Socket.IO server.
    // http[s]://<domain>:<port>[/<namespace>]
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
});

function getNsList() {
    //Empty Function
    return null;
}

function getModList(ns) {
    //Empty Function
    return null;
}

function getModInfo(mod) {
    //Empty Function
    return null;
}

function harden(mod) {
    //Empty Function
    return null;
}