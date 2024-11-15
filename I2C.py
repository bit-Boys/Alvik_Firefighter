from arduino_alvik import ArduinoAlvik
from time import sleep_ms
import sys
from machine import I2C


i2c = I2C(0, freq=400000)          # create I2C at 400kHz

alvik = ArduinoAlvik()
alvik.begin()


address = i2c.scan()[0]     # usually 43
sleep_ms(500)


while True:

  command = i2c.readfrom(address, 4)  # read in 4 bytes
  print(command)
  command = ""

  if command == "F":
    print("Got Command")
      
  

