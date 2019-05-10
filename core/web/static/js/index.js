console.log('loaded');

$(document).ready(function() {
    // Connect to the Socket.IO server.
    // http[s]://<domain>:<port>[/<namespace>]
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // Event handler for new connections.
    // The callback function is invoked when a connection with the
    // server is established.
    socket.on('connect', function() {
        socket.emit('my_event', {data: 'I\'m connected!'});
    });
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