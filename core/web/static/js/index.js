//Page is ready

// test code
var module_names = [
    Object.create({ name: "Disable_File_Sharing", state: "open" }),
    Object.create({ name: "Disable_RDP", state: "open" }),
    Object.create({ name: "Other_Harden_Method", state: "open" })
]
// test code 

toggleDiv = (obj) => {
    $("#" + obj.name + "_drawer").slideToggle("slow");
    
    // Todo: Add ajax query

    // test code
    $("#" + obj.name + "_logs").val("Executing...");
    // test code
}

$(function () {
    module_names.forEach(elem => {
        $("#" + elem.name + "_btn").click(() => {
            $("#" + elem.name + "_ico").toggleClass('rotated');
            toggleDiv(elem);
        })
    })
})