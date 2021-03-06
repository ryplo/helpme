import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math
import os
import pypd
import RPi.GPIO as GPIO
import pygame

pygame.init()
pygame.mixer.init()
sounda=pygame.mixer.Sound("beep-07.wav")

pypd.api_key = "xx3gyxWCgxhQtvxs1K6B"

# pin for switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# upon startup, resolve all unresolved incidents
open_incidents = pypd.Incident.find(statuses=["triggered"])
for incident in open_incidents:
    print ("incident: " + incident.get('id'))
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

highThreshold=1.5
name="Gurshan"
lowThreshold=.5
beginTime=0
endTime=0
elapsedTime=0

# Master loop, resolved by hardware switch
while True:
    if (GPIO.input(4) == 1):
      if imu.IMURead():
        # x, y, z = imu.getFusionData()
        # print("%f %f %f" % (x,y,z))
        data = imu.getIMUData()
        accel = data["accel"]

        # Waiting for fall to happen
        
        if abs(accel[0])>highThreshold or abs(accel[1])>highThreshold or abs(accel[2])>highThreshold:
          # Once fall occurs, create incident
          beginTime=time.clock()
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
          time.sleep(5)
          #While patient is on ground continue to play beep
          while abs(accel[0])<lowThreshold or abs(accel[1])<lowThreshold or abs(accel[2])<lowThreshold:
            sounda.play(-1)
            imu.IMURead()
            data = imu.getIMUData()
            accel = data["accel"]
            print("r: %f p: %f y: %f" % ((accel[0]), 
            (accel[1]), (accel[2])))
          #Once patient is no longer still on ground, stop beep, end time, resolve ticket
          endTime=time.clock()
          elapsedTime=endTime-beginTime
          open_incident = pypd.Incident.find_one(statuses=["triggered"])
          pypd.Incident.create_note(open_incident, name + " got back up")
          pypd.Incident.resolve(open_incident, "lo.rachel8@gmail.com")
          #Patient is alive, create new incident

          pypd.Event.create(data={
            'service_key': 'c7f3b642055b4a76b875a4072e9f945e',
            'event_type': 'trigger',
             'description':name + 'has gotten up',
            'contexts': [
                  {
                      'type': 'link',
                      'href': 'http://bushdid7111.pagerduty.com',
                      'text': 'View on PD',
                  },
            ],
          })
          open_low_incident = pypd.Incident.find_one(statuses=["triggered"])
          pypd.Incident.create_note(open_low_incident, name + " recently fell and should be checked up on")
          
        time.sleep(poll_interval*1.0/1000.0)

