$(document).ready(initializePage);

function Module(moduleName, moduleDesc, moduleSource, socket) {
    /*
    Module object.
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

    this.writeLog = (message) => {
        var currentTime = new Date().toLocaleTimeString().split(' ')[0];
        this.logs.val(this.logs.val() + currentTime + " > " + message + "\n");
    }

    this.render = function () {
        var modules = $("#modules");
        modules.append('<div class="module-box deep" style="margin-bottom: 20px" id="' + this.name + '_div">\
            <div class="row">\
                <div class="col-8 d-flex justify-content-between" id="' + this.name + '_area">\
                    <div class="mr-auto p-2 text-left">\
                        <h6>' + this.name + '</h6>\
                        <p class="text-muted" style="font-size: 13px; margin-bottom:0">' + this.desc + '</p>\
                    </div>\
                </div>\
                <div class="col-4 text-right mt-1">\
                    <a id="' + this.name + '_btn"><i style="font-size: 52px"\
                            id="' + this.name + '_ico" class="fas fa-arrow-circle-right"></i></a>\
                </div>\
                <div class="container-fluid mt-1">\
                    <div class="drawer-content" id="' + this.name + '_drawer">\
                        <textarea class="logs consolas font-small text-muted" name="logs"\
                            id="' + this.name + '_logs" cols="30" rows="5" readonly></textarea>\
                        <button class="btn btn-block" style="border-width: 0; margin-top: 1%;" \
                            id="' + this.name + '_execute_btn">Run<i class="fas fa-cog ml-1"></i></button>\
                    </div>\
                </div>\
            </div>\
        </div>');

        // Access DOM
        this.div = $("#" + this.name + "_div")
        this.area = $("#" + this.name + "_area")
        this.drawer = $("#" + this.name + "_drawer")
        this.logs = $("#" + this.name + "_logs")
        this.button = $("#" + this.name + "_btn")
        this.icon = $("#" + this.name + "_ico")
        this.execute_btn = $("#" + this.name + "_execute_btn");

        this.logs.val("[#]: " + this.source + "\n");
        this.button.click(() => {
            this.openDrawer(200);
        });
        this.area.click(()=>{
            this.openDrawer(200);
        });
        this.socket.on(this.name + "_log", (data) => {
            this.writeLog(data.msg);
            if (data.state == "success")
                this.execute_btn.find(".fa-cog").removeClass('rotate_cogs fa-cog').addClass("fa-check");
            else if (data.state == "error")
                setTimeout(() => {this.execute_btn.find(".fa-cog").removeClass('rotate_cogs')}, 400);
        });
        this.execute_btn.click(() => {
            this.socket.emit("harden", this.name);
            this.execute_btn.find(".fa-cog").addClass('rotate_cogs');
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
            });
        });
    });
}

function initializePage() {
    AOS.init(); // AOS scroll library
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.emit('get_namespaces', {});  // Request namespace list
    socket.on('get_namespaces', (data) => {  // Add namespace string to html
        var { namespaces } = data;
        namespaces.forEach(namespace => {
            $("#namespaces").append('<li class="dropdown-item">' + namespace + '</li>');
        });

        // Getting current namespace from server
        socket.emit('get_current_namespace', {});
        socket.on('get_current_namespace', (data) => {
            $("#current_namespace").text(data.current_namespace);
            socket.emit('send_current_namespace', data.current_namespace);
        });

        // Namespace selection
        $("#namespaces li").click(function (e) {
            // Don't reload page
            e.preventDefault()   
            $("#current_namespace").text($(this).text());
            // 'send_current_namespace' event, will trigger 'get_module'            
            socket.emit('send_current_namespace', $(this).text());
        });

        // Getting modules
        socket.on('get_module', (data) => {
            $("#modules").empty();
            data.forEach(elem => {
                // Render modules
                var { name, desc, source } = elem
                var mod = new Module(name, desc, source, socket);
                mod.render();
            });
            // Remove loading screen when page is ready
            $(".overlay").fadeOut("slow");
            search(socket);
        });
    });
}