import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math

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

f = open('Walking.csv',"w")

poll_interval = imu.IMUGetPollInterval()
print("Recommended Poll Interval: %dmS\n" % poll_interval)
count = 0
initTime= time.time()
print(initTime)
while (time.time()-initTime<10): 
  if imu.IMURead():
    # x, y, z = imu.getFusionData()
    # print("%f %f %f" % (x,y,z))
    data = imu.getIMUData()
    accel = data["accel"]
    gyr = data["gyro"]
    compass = data["compass"]
##    print("r: %f p: %f y: %f" % (fusionPose[0], 
##        fusionPose[1], fusionPose[2]))
    f.write(str(accel[0])+","+str(accel[1])+","+str(accel[2])+","+str(gyr[0])+","+str(gyr[1])+","+str(gyr[2])+","+str(compass[0])+","+str(compass[1])+","+str(compass[2])+"\n")
    count+=1
    time.sleep(poll_interval*1.0/1000.0)
##print(time.time()-initTime)
f.close()
