/*
Module divs
Javascript will use:
  - module_name_div
  - module_name_btn (Button trigger)
  - module_name_ico (for animation)
  - module_name_drawer
  - module_name_logs (logs text area)
*/
function getModuleBox(name, desc) {
	return '<div class="module-box deep" style="margin-bottom: 20px;" id="' + name + '_div" data-aos="fade-up">\
            <div class="row">\
                <div  class="col-9 d-flex justify-content-between" id="' + name + '_area">\
                    <div class="mr-auto p-2 text-left">\
                        <h6 style="word-break: break-all;">' + name + '</h6>\
                        <p class="text-muted" style="font-size: 13px; margin-bottom:0">' + desc + '</p>\
                    </div>\
                </div>\
                <div class="col-3 text-right mt-1">\
                    <a id="' + name + '_btn"><i style="font-size: 52px"\
                            id="' + name + '_ico" class="fas fa-arrow-circle-right"></i></a>\
                </div>\
                <div class="container-fluid mt-1">\
                    <div class="drawer-content" id="' + name + '_drawer">\
                        <textarea class="logs consolas font-small text-muted" name="logs"\
                            id="' + name + '_logs" cols="30" rows="5" readonly></textarea>\
                        <button class="btn btn-block" style="border-width: 0; margin-top: 1%;" \
                            id="' + name + '_execute_btn">Run<i class="fas fa-cog ml-1"></i></button>\
                    </div>\
                </div>\
            </div>\
        </div>'
}
