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

function Module(moduleName) {
    this.name = moduleName
    this.div = $("#" + moduleName + "_div")
    this.drawer = $("#" + moduleName + "_drawer")
    this.logs = $("#" + moduleName + "_logs")
    this.button = $("#" + moduleName + "_btn")
    this.icon = $("#" + moduleName + "_ico")

    this.openDrawer = (animationSpeed) => {
        this.icon.toggleClass("rotated");
        this.drawer.slideToggle({
            duration: animationSpeed
        });
    }

    this.runSocketio = () => {
        // Todo: Add socket io query or connetion stuff
        return null;
    }

    this.logWrite = (message) => {
        this.logs.val(this.logs.val() + message + "\n");
    }
}

// <-- Test code
module_names = [
    new Module("Disable_File_Sharing"),
    new Module("Disable_RDP"),
    new Module("Other_Harden_Method")
]
// Test code -->

//Page is ready
$(function () {
    AOS.init();
    $("#modulecount").text(module_names.length);
    module_names.forEach(elem => {  // Listen click events
        elem.button.click(() => {
            elem.openDrawer(250);
        })
    })
})


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

