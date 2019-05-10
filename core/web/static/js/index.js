console.log('loaded');

$(document).ready(function() {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    socket.on('connect', function() {
        socket.emit('my_event', {data: 'I\'m connected!'});
    });
    socket.on('my_response', function(msg) {
    $('#log').append('<br>' + $('<div/>').text('Received #' + msg.count + ': ' + msg.data).html());
    });
 
    socket.on('my_pong', function() {
    var latency = (new Date).getTime() - start_time;
    ping_pong_times.push(latency);
    ping_pong_times = ping_pong_times.slice(-30);
    var sum = 0;
    for (var i = 0; i < ping_pong_times.length; i++)
    sum += ping_pong_times[i];
    $('#ping-pong').text(Math.round(10 * sum / ping_pong_times.length) / 10);
    });
});

function getNsList() {
    return null;
}

function getModList(ns) {
    return null;
}

function getModInfo(mod) {
    return null;
}

function harden(mod) {
    return null;
}