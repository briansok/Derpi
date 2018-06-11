from django.core.management.base import BaseCommand, CommandError
from sensors.models import Sensors
from channels import Group

class Command(BaseCommand):
    help = 'This command gets the sensor output data through the websocket'

    def handle(self, *args, **options):
        self.stdout.write("Sending packages")
        output_sensors = Sensors.objects.filter(sensor_types="OU")

        for output_sensor in output_sensors:
            Group("sensors-%s" % "").send({
             "text": '{"id":%s,"type": "OU","read": 1}' % output_sensor.id,
            })

