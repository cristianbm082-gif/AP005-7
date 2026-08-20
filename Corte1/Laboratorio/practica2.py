from machine import Pin
from time import sleep

led = Pin(2,Pin.OUT)

tiempo = 5

for i in range (5):
    led.on()
    sleep(tiempo)
    
    led.off()
    sleep(tiempo)
    
    tiempo = tiempo -1
