import pypd
import os
import RPi.GPIO as GPIO

pypd.api_key = "xx3gyxWCgxhQtvxs1K6B"

# pin for switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# upon startup, resolve all unresolved incidents
open_incidents = pypd.Incident.find(statuses=["triggered"])
for incident in open_incidents
    pypd.Incident.resolve(incident, "lo.rachel8@gmail.com")

# triggered = False
# while True:
if True: # if Sensor.fall == True
    pypd.Event.create(data={
        'service_key': '266cc74b1bef4ad8be210d0819a436f8',
        'event_type': 'trigger',
        'description': 'this is a trigger event!',
        'contexts': [
              {
                  'type': 'link',
                  'href': 'http://bushdid7111.pagerduty.com',
                  'text': 'View on PD',
              },
        ],
    })
triggered = True
while (GPIO.input(4) == 1):
    os.system ("omxplayer beep-05.wav")
open_incidents = pypd.Incident.find(statuses=["triggered"])
pypd.Incident.resolve(incident, "lo.rachel8@gmail.com")
