import machine
import time

led = machine.Pin(23, machine.Pin.OUT)

print("Iniciando o teste do LED...")


while True:
    led.value(1)
    print("LED Ligado")
    time.sleep(1)
    
    led.value(0)
    print("LED Desligado")
    time.sleep(1)