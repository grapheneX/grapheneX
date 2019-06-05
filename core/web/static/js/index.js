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
        modules.append(getModuleBox(this.name, this.desc));

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
        this.area.click(() => {
            this.openDrawer(200);
        });
        this.execute_btn.click(() => {
            this.execute_btn.find(".fa-cog").addClass("rotate_cogs");
            this.socket.emit("harden", this.name); 
        });
        this.socket.on(this.name + "_log", (data) => {
            this.writeLog(data.msg);
            if (data.state == "success")
                this.execute_btn.find(".fa-cog").removeClass('rotate_cogs fa-cog').addClass("fa-check");
            else if (data.state == "error")
                this.execute_btn.find(".fa-cog").removeClass('rotate_cogs').addClass("fa-times-circle");
        });
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


saveModal = () => {
    console.log($("#amod_ns_list").find(".active").text())
}

prepareModal = () => {
        $("#addModuleModal").on('show.bs.modal', function () {
            $("#openModal").find('.fa-plus').addClass('rotate_cogs')
            var _addNsElem = $("#amod_ns_list > li").last();
            var _input = $("<input class='form-control ' id='amod_new_ns' \
                            style='padding: .75rem 1.25rem; height: auto;'\
                            placeholder='Namespace name...'\
                            type='text' />")
    
            _addNsElem.click(() => {
                _addNsElem.before(_input);
                _addNsElem.hide();
                _input.val('');
                _input.focus();
                _input.on('keypress', function(e) {
                    if (e.keyCode == 13) {  // When press enter
                        var newNsText = _input.val();
                        /* 
                            Todo send new namespace with socketio
                        */
                        var newNsElem = $("<li class='list-group-item'>"+ newNsText +"</li>")
                        _input.replaceWith(newNsElem)
                        newNsElem.addClass('active');
                        _addNsElem.removeClass('active');
                        _addNsElem.show();
                    }
                })
            }) 
        })
        $("#addModuleModal").on('hidden.bs.modal', function () {
            $("#openModal").find('.fa-plus').removeClass('rotate_cogs')
        })
}

function initializePage() {
    AOS.init(); // AOS scroll library
    prepareModal();
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.emit('get_namespaces', {});  // Request namespace list
    socket.on('get_namespaces', (data) => {  // Add namespace string to html
        var { namespaces } = data;
        namespaces.forEach(namespace => {
            $("#namespaces").append('<li class="dropdown-item">' + namespace + '</li>');
            $("#amod_ns_list").prepend('<li class="list-group-item">' + namespace + '</li>');
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