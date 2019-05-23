$(document).ready(initializePage);


function Module(moduleName, moduleDesc, moduleSource, socket) {
    /*
    This is a Module object.
    */
    this.name = moduleName;
    this.socket = socket;
    this.desc = moduleDesc;
    this.source = moduleSource;
    this.socket = socket;

    this.openDrawer = (animationSpeed) => {
        this.icon.toggleClass("rotated");
        this.drawer.slideToggle({
            duration: animationSpeed
        });
    }

    this.logWrite = (message) => {
        this.logs.val(this.logs.val() + message + "\n");
    }

    this.harden = () => {
        // Todo: Add socket io query or connetion stuff
        return null
    }

    this.render = function () {
        var modules = $("#modules");
        modules.append(getModuleBox(this.name, this.desc));

        // Access DOM
        this.div = $("#" + this.name + "_div")
        this.drawer = $("#" + this.name + "_drawer")
        this.logs = $("#" + this.name + "_logs")
        this.button = $("#" + this.name + "_btn")
        this.icon = $("#" + this.name + "_ico")

        this.logWrite(this.source);
        this.button.click(() => {  // Listening click event
            this.openDrawer(250);  // open textbox
        })
    }
}

search = function (socket) {
    $("#module_search").on("keyup", function () {
        query = $(this).val();
        socket.emit('search_module', { query: query });
        socket.on('search_module', (data) => {
            $("#modules").empty();
            data.result.forEach(elem => {
                var { name, desc, source } = elem
                var mod = new Module(name, desc, source, socket);
                mod.render();
            })
        })
    })
}


function initializePage() {
    AOS.init(); // AOS scroll lib


    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.emit('get_namespaces', {})  // Request namespace list
    socket.on('get_namespaces', (data) => {  // Added namespace string to html
        var { namespaces } = data;
        namespaces.forEach(namespace => {
            $("#namespaces").append('<li class="dropdown-item">' + namespace + '</li>');
        })

        // Getting current namespace from server
        socket.emit('get_current_namespace', {});
        socket.on('get_current_namespace', (data) => {
            $("#current_namespace").text(data.current_namespace);
            socket.emit('send_current_namespace', data.current_namespace);
        })

        // Namespcae selection
        $("#namespaces li").click(function (e) {
            e.preventDefault()  // no reload page 
            $("#current_namespace").text($(this).text());

            // 'send_current_namespace' event, will trigger 'get_module'. See server side            
            socket.emit('send_current_namespace', $(this).text());
        })

        /* Namespace stuff finished */

        // Getting modules
        socket.on('get_module', (data) => {
            $("#modules").empty();
            data.forEach(elem => {
                // Render modules
                var { name, desc, source } = elem
                var mod = new Module(name, desc, source, socket);
                mod.render();
            })
            console.log("Page is ready");
            $(".overlay").fadeOut("slow");  // remove loading screen
            search(socket);
        })
    })

}