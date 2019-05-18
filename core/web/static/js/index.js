$(document).ready(initializePage);
$(document).ready(onNamespaceSelected);

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

    this.harden = (socket) => {
        // Todo: Add socket io query or connetion stuff
        return null
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

function initializePage() {
    AOS.init();

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', () => {
        // example emit call
        socket.emit("connected", document.domain);
    })

    $("#modulecount").text(module_names.length);
    module_names.forEach(elem => {  // Listen click events
        elem.button.click(() => {
            elem.openDrawer(250);
        })
        elem.harden(socket)
    })
}

function onNamespaceSelected() {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    $('.dropdown-item').click(function(){
        socket.emit("namespace",$(this).text());
    });

    socket.on('modules', function(modules){
        console.log(modules);
    });
}