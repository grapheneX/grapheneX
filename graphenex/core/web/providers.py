from graphenex.core.web import auth_socketio, socketio, emit
from graphenex.core.utils.sysinfo import SysInformation


@socketio.on('get_network_info')
@auth_socketio
def send_network_info():
    masks = SysInformation.get_network_info()
    emit('get_network_info', masks)
