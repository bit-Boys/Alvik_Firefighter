# Micropython to run on the Alvik. Just listens for I2C connections and does something when recieved. 
# Format should be like F10.  => Forward 10 cm. (Period is necessary to tell you are at the end)
# (F)orward, (B)ackward, Turn (L)eft, Turn (R)ight. Unit in degrees of robot if turning.


from arduino_alvik import ArduinoAlvik
from time import sleep_ms
import sys
from machine import I2C


i2c = I2C(0, freq=400000)          # create I2C at 400kHz

alvik = ArduinoAlvik()
alvik.begin()


address = i2c.scan()[0]     # usually 43
sleep_ms(500)

command = b''
data = b''
while True:

  data = i2c.readfrom(address, 2)  # read in 2 bytes MUST BE SENT IN 2 BYTE CHUNKS

  command = data.split()[0]
  print(command)


  if command == "F":
    print("Forward")
    dis = data[:data.index(".")]        # gets everything until dot
    alvik.move(dis)
      
  elif command == "B":
    dis = data[:data.index(".")]
    alvik.move(-dis)
 
  elif command == "L":
    deg = data[:data.index(".")]
    alvik.rotate(-deg)
    

  elif command == "R":
    deg = data[:data.index(".")]
    alvik.rotate(deg)

