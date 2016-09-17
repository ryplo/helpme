import pypd
import os
pypd.api_key = "xx3gyxWCgxhQtvxs1K6B"
# find incidents, resolve the unresolvd ones.

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
    os.system ("omxplayer beep-05.wav")
