function refresh() {
    socket.on('get_network_info', function(data) {
        data.forEach((mask) => {
            /*
                mask[0] = name
                mask[1] = recv
                mask[2] = send
                mask[3] = slug/id
            */
            id = "#" + mask[3]
            $(id + "_send").text(mask[2])
            $(id + "_recv").text(mask[1])
        })
    })
    socket.emit('get_network_info')
}

$(document).ready(function() {
    setInterval(refresh, 3000)
})