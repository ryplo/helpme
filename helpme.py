import pypd
import os
pypd.api_key = "xx3gyxWCgxhQtvxs1K6B"
# find incidents, resolve the unresolvd ones.

while True:
    triggered = False
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
    while triggered == True:
        file = ' /Users/rachello/dev/helpme/beep-05.wav'
        os.system ('mplayer' + file)
        if True:
            triggered = False
