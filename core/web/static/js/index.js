$(document).ready(initializePage);


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


addModule = (option) => {
/* 
    This function, create new module div end other props in index.html
    option will be:
    
        addModule({
            name: 'Harden_Method',
            desc: 'Harden_Method information,
            socket: socketobj
        });

        Note: socket variable will be sockett io conection object

        remember this function return type is Module object
*/
    var {name, desc, socket} = option;
    var modules = $("#modules");
    modules.append('<div class="module-box deep" style="margin-top: 80px;" id="' + name +'_div">\
        <div class="row">\
            <div class="col-8 d-flex justify-content-between">\
                <div class="mr-auto p-2 text-left">\
                    <h6>' + name + '</h6>\
                    <p class="text-muted" style="font-size: 12px; margin-bottom:0">' + desc + '</p>\
                </div>\
            </div>\
            <div class="col-4 text-right mt-1">\
                <a id="' + name + '_btn"><i style="font-size: 52px"\
                        id="' + name + '_ico" class="fas fa-arrow-circle-right"></i></a>\
            </div>\
            <div class="container-fluid mt-1">\
                <div class="drawer-content" id="' + name + '_drawer">\
                    <textarea class="logs consolas text-muted" name="logs"\
                        id="' + name + '_logs" cols="30" rows="5" disabled></textarea>\
                </div>\
            </div>\
        </div>\
    </div>')
    var mod= new Module(name);
    mod.button.click(()=> {
        mod.openDrawer(250);
    })
    mod.harden(socket);

    return mod;
}



function initializePage() {
    AOS.init();


    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', () => {
        // example emit call
        socket.emit("connected", document.domain);
    })
    socket.emit('get_namespaces', {})  // Request namespace list
    socket.on('get_namespaces', (data) => {  // Added namespace string to html
        var { namespaces } = data;
        namespaces.forEach(namespace => {
            $("#namespaces").append('<a class="dropdown-item" href="#">' + namespace + '</a>');
        })

        // Getting current namespace from server
        socket.emit('get_current_namespace', {});
        socket.on('get_current_namespace', (data) => {
            $("#current_namespace").text(data.current_namespace);
        })
    })
}

