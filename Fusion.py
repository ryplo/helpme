import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math
import os
import pypd
pypd.api_key = "xx3gyxWCgxhQtvxs1K6B"

# pin for switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# upon startup, resolve all unresolved incidents
open_incidents = pypd.Incident.find(statuses=["triggered"])
for incident in open_incidents
    pypd.Incident.resolve(incident, "lo.rachel8@gmail.com")

SETTINGS_FILE = "RTIMULib"

print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
  print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

print("IMU Name: " + imu.IMUName())

if (not imu.IMUInit()):
    print("IMU Init Failed")
    sys.exit(1)
else:
    print("IMU Init Succeeded")

# this is a good time to set any fusion parameters

imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()
print("Recommended Poll Interval: %dmS\n" % poll_interval)

highThreshold=2
name="Gurshan"
lowThreshold=1
beginTime
endTime
elapsedTime

while (GPIO.input(4) == 1):
  if imu.IMURead():
    # x, y, z = imu.getFusionData()
    # print("%f %f %f" % (x,y,z))
    data = imu.getIMUData()
    accel = data["accel"]
    if abs[accel[0]]>highThreshold or abs[accel[1]]>highThreshold or abs[accel[2]]>highThreshold:
      beginTime=time.clock()
      os.system ("omxplayer beep-05.wav")
      pypd.Event.create(data={
        'service_key': '266cc74b1bef4ad8be210d0819a436f8',
        'event_type': 'trigger',
        'description':name + 'has fallen',
        'contexts': [
              {
                  'type': 'link',
                  'href': 'http://bushdid7111.pagerduty.com',
                  'text': 'View on PD',
              },
        ],
      })
      while abs[accel[0]]<lowThreshold or abs[accel[1]]<lowThreshold or abs[accel[2]]<lowThreshold:
        
    time.sleep(poll_interval*1.0/1000.0)
    

