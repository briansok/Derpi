from channels import Group
from channels import Channel
from channels.sessions import channel_session
from django.contrib.auth.decorators import login_required
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
from sensors.models import Sensors
import json

# Connected to websocket.connect
@channel_session
@channel_session_user_from_http
def ws_connect(message):

    # if message.user.is_authenticated():
    print(message.user)
    message.reply_channel.send({"accept": True})

    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip("/")

    # Save room in session and add us to the group
    message.channel_session['room'] = room
    Group("sensors-%s" % room).add(message.reply_channel)

# Connected to websocket.receive
@channel_session
@channel_session_user
def ws_message(message):
    Group("sensors-%s" % message.channel_session['room']).send({
            "text": message['text'],
    })

    data = message['text']

    sensor_data = json.loads(data)

    if sensor_data['read'] == 0:
        id = sensor_data['id']
        value = sensor_data['value']

        sensor = Sensors.objects.get(id=id)
        sensor.value = value
        sensor.save()

        print(message['text'])

# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group("sensors-%s" % message.channel_session['room']).discard(message.reply_channel)

