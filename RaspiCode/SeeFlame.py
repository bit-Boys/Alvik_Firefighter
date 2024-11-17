# Navigates through the maze, detecting candles and going toward them

import smbus
import time


bus = smbus.SMBus(0)
address = 0x60   # May change
command_address = 0x00   # Keep here unless we need to send a lot of data, like "page" of a book


data = b'F2.'

bus.write_byte_data(address, command_address, data)



# Scan for the position of the candle flame in the maze

# Turn so that it is in the middle of the screen

# Take "steps" forward, waiting until flame is extinguished, assumed by the fact that it can't be recongnized


