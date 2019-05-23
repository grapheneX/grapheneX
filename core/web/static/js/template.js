function getModuleBox(name, desc) {
	return '<div class="module-box deep" style="margin-bottom: 20px" id="' + name + '_div">\
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
        </div>'
}