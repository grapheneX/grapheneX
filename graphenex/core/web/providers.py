from graphenex.core.web import auth_socketio, socketio, emit
from graphenex.core.utils.helpers import Information


@socketio.on('get_network_info')
@auth_socketio
def send_network_info():
    masks = Information.get_network()
    emit('get_network_info', masks)

