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

    // Event handler for server sent data.
    // The callback function is invoked whenever the server emits data
    // to the client. The data is then displayed in the "Received"
    // section of the page.
    socket.on('my_response', function(msg) {
    $('#log').append('<br>' + $('<div/>').text('Received #' + msg.count + ': ' + msg.data).html());
    });

    // Handler for the "pong" message. When the pong is received, the
    // time from the ping is stored, and the average of the last 30
     // samples is average and displayed.
    socket.on('my_pong', function() {
    var latency = (new Date).getTime() - start_time;
    ping_pong_times.push(latency);
    ping_pong_times = ping_pong_times.slice(-30); // keep last 30 samples
    var sum = 0;
    for (var i = 0; i < ping_pong_times.length; i++)
    sum += ping_pong_times[i];
    $('#ping-pong').text(Math.round(10 * sum / ping_pong_times.length) / 10);
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