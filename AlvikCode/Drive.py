# We should test this, using lidar to navigate, and obviously much better to run on alvik itself.


from arduino_alvik import ArduinoAlvik
import time


alvik = ArduinoAlvik()
alvik.begin()

# set up
alvik.rotate(-45)



distances = alvik.get_distance()
wall = distances[4]
print(wall)

while distances[4] > 6 or distances[4] < 2:
  alvik.move(3.0)
  distances = alvik.get_distance()
  print("in loop 1")

alvik.rotate(45)


while True:
  

  # scan phase
  alvik.rotate(-45)
  distances = alvik.get_distance()
  wall = distances[4]

  while distances[4] > 8 or distances[4] < 2:
      distances = alvik.get_distance()
      alvik.rotate(-10)

  # straight ahead
  alvik.rotate(45)

  
  distances = alvik.get_distance()
  if distances[2] < 8:
    print("left turn ahead")
    while distances[4] > 12 or distances[2] < 8:
      distances = alvik.get_distance()
      alvik.rotate(8)

  alvik.move(5) # move 5 cm to next increment
