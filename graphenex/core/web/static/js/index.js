$(document).ready(initializePage);

var socket;

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
            if (data.msg != null)
                this.writeLog(data.msg);
            if (data.state == "success")
                this.execute_btn.find(".fa-cog").removeClass('rotate_cogs fa-cog').addClass("fa-check");
            else if (data.state == "error")
                this.execute_btn.find(".fa-cog").removeClass('rotate_cogs').addClass("fa-times-circle");
        });
    }
}

/* Search module event */
search = function () {
    $("#module_search").on("keyup", function () {
        query = $(this).val();
        setTimeout(() => {
            socket.emit('search_module', { query: query });
            socket.on('search_module', (data) => {
                $("#modules").empty();
                data.result.forEach(elem => {
                    var { name, desc, source } = elem
                    var mod = new Module(name, desc, source, socket);
                    mod.render();
                });
            });
        }, 500)

    });
}

/* New module save event */
saveModal = () => {
    socket.emit("add_module", {
        "ns": $("#amod_ns_list").find(".active").text().trim(),
        "name": $("#amod_name").val(),
        "desc": $("#amod_desc").val(),
        "cmd": $("#amod_cmd").val(),
        "su": $('#amod_su').prop("checked")
    });
}

/* Prepare the new module modal */
prepareModal = () => {
    $("#addModuleModal").on('show.bs.modal', function () {
        $("#openModal").find('.fa-plus').addClass('rotate_cogs')
        var _addNsElem = $("#amod_ns_list > li").last();
        var _input = $("<input class='form-control ' id='amod_new_ns' \
                            style='padding: .75rem 1.25rem; height: auto;'\
                            placeholder='Namespace name...'\
                            type='text' />")
        _addNsElem.click(() => {
            if ($('#amod_new_ns').length == 0)
                _addNsElem.before(_input);
            _addNsElem.hide();
            _input.val('');
            _input.focus();
            _input.focusout(function () {
                _input.trigger(jQuery.Event('keypress', { keyCode: 13, which: 13 }));
            })
            _input.on('keypress', function (e) {
                if (e.keyCode == 13) { // Pressed on enter key
                    var newNsText = _input.val();
                    var newNsElem = $("<li class='list-group-item' id='new_ns_" + newNsText + "'>" +
                        newNsText + "</li>")
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

/* Show message with modal */
createMessage = (data) => {
    var messageClass = 'text-white bg-' + data.tag
    var _modal = $("#messageModal");
    _modal.modal({ backdrop: false });  // don't touch background opacity
    _modal.find(".modal-content").addClass(messageClass);
    _modal.find(".modal-content").text(data.content);
    var sec = typeof data.duration === 'undefined' ? 1000 : data.duration;
    setTimeout(() => {
        _modal.modal("hide");
        _modal.find(".modal-content").removeClass(messageClass);
    }, sec)
}

/* Initialize the page & connect */
function initializePage() {
    AOS.init(); // AOS scroll library
    prepareModal();
    socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('log_message', (data) => {
        createMessage(data);
    })
    // Request namespace list
    socket.emit('get_namespaces', {});
    // Add namespace string to HTML
    socket.on('get_namespaces', (data) => {
        var { namespaces } = data;
        $("#namespaces").empty()
        namespaces.forEach(namespace => {
            $("#namespaces").append('<li class="dropdown-item">' + namespace + '</li>');
            if ($("#ns_list_" + namespace).length == 0)
                $("#amod_ns_list").prepend('<li class="list-group-item" id="ns_list_' + namespace +
                    '">' + namespace + '</li>');
        });
        socket.emit('get_current_namespace', {});
        // Namespace selection
        $("#namespaces li").click(function (e) {
            // Don't reload page
            e.preventDefault()
            $("#current_namespace").text($(this).text());
            // 'send_current_namespace' event, will trigger 'get_module'            
            socket.emit('send_current_namespace', $(this).text());
        });
    });

    // Getting current namespace from server
    socket.on('get_current_namespace', (data) => {
        $("#current_namespace").text(data.current_namespace);
        socket.emit('send_current_namespace', data.current_namespace);
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
        search();
    });

    // Added new module
    socket.on('new_module_added', (data) => {
        $("#addModuleModal").modal('toggle');
        $("#addModuleModal").find("input,textarea,select").val('').end();
        $('[id^="new_ns_"]').remove();
        $("#modulecount").text(data);
        socket.emit('get_namespaces', {});
    });

    $('#amod_su_label').click(() => {
        $('#amod_su').click();
    });
}
