# Micropython to run on the Alvik. Just listens for I2C connections and does something when recieved. 
# Format should be like F10.  => Forward 10 cm. (Period is necessary to tell you are at the end)
# (F)orward, (B)ackward, Turn (L)eft, Turn (R)ight. Unit in degrees of robot if turning.


from arduino_alvik import ArduinoAlvik
from time import sleep_ms
import sys
import machine
from machine import Pin, I2C

A4 = 11                                         # ESP32 pin11 SDA -> nano A4
A5 = 12                                         # ESP32 pin12 SCL -> nano A5
ESP32_SDA = Pin(A4, Pin.OUT)                    # ESP32_SDA
ESP32_SCL = Pin(A5, Pin.OUT)                    # ESP32_SCL

print("works")
          
alvik = ArduinoAlvik()
#alvik.begin()


i2c = machine.SoftI2C(ESP32_SCL, ESP32_SDA, freq=50000)   # create I2C at 100kHz
i2c.init(ESP32_SCL, ESP32_SDA, freq=50000)


scans = []
while True:
  scans = i2c.scan()
  print(scans)
  sleep_ms(25)

  if scans != []:
    print("WORKED GOT")
    print(scans[0])
    try:
      for i in range(len(scans)):
        val = i2c.readfrom_mem(scans[i], 0x08 , 1) 
        print(val)
    except Exception as e:
      print("Errored")
      print(e)


address = scans[0]

print("Scanning...")

count = 0
command = b""


# read
while True:

  command = i2c.readfrom(address, 1)  # read in 4 bytes
  print(command)
  sleep_ms(100)
      
  


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

