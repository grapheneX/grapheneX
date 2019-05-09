

// test code
var module_names = [
    Object.create({ name: "Disable_File_Sharing", state: "open" }),
    Object.create({ name: "Disable_RDP", state: "open" }),
    Object.create({ name: "Other_Harden_Method", state: "open" })
]
// test code 

toggleDiv = (obj) => {
    $("#" + obj.name + "_drawer").slideToggle({
        duration: 250
    });
    
    // Todo: Add ajax query

    // test code
    var logs = $("#" + obj.name + "_logs");
    logs.val("22:29:34 > core.utils.commnads > INFO > Executing...\n"); 
    logs.val(logs.val() + " > netsh advfirewall firewall set rule group=\"File and Printer Sharing\" new enable=No \n")
    logs.val(logs.val() + "22:29:35 > core.utils.commnads > INFO > Done.\n")
    // test code
}

//Page is ready
$(function () {
    AOS.init();
    module_names.forEach(elem => {
        $("#" + elem.name + "_btn").click(() => {
            $("#" + elem.name + "_ico").toggleClass('rotated');
            toggleDiv(elem);
        })
    })
})