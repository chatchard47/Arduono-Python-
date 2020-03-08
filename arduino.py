from nanpy import SerialManager
from nanpy import ArduinoApi
import time
connection = SerialManager(device='COM3')
a = ArduinoApi(connection=connection)
a.pinMode(13, a.OUTPUT)
while 1:
    a.digitalWrite(13, a.HIGH)
    time.sleep(5)
    a.digitalWrite(13, a.LOW)
    time.sleep(5)
    
