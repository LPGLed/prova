
print("Ciao Marco!!!!!!!")

print("forza Roma!!!!!!!")

firmware_url = "https://github.com/LPGLed/prova"
from machine import Pin
from time import sleep

led = Pin(2,Pin.OUT)

while True:
    led.value(0)
    sleep(2)
    led.value(1)
    sleep(2)
