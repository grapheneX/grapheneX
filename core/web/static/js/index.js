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
        modules.append('<div class="module-box deep" style="margin-bottom: 20px" id="' + this.name + '_div">\
            <div class="row">\
                <div class="col-8 d-flex justify-content-between">\
                    <div class="mr-auto p-2 text-left">\
                        <h6>' + this.name + '</h6>\
                        <p class="text-muted" style="font-size: 12px; margin-bottom:0">' + this.desc + '</p>\
                    </div>\
                </div>\
                <div class="col-4 text-right mt-1">\
                    <a id="' + this.name + '_btn"><i style="font-size: 52px"\
                            id="' + this.name + '_ico" class="fas fa-arrow-circle-right"></i></a>\
                </div>\
                <div class="container-fluid mt-1">\
                    <div class="drawer-content" id="' + this.name + '_drawer">\
                        <textarea class="logs consolas text-muted" name="logs"\
                            id="' + this.name + '_logs" cols="30" rows="5" disabled></textarea>\
                    </div>\
                </div>\
            </div>\
        </div>')

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