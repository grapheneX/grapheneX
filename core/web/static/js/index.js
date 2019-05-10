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