from machine import Pin
from dht import DHT22
import time

# Configuração do Sensor DHT22 no pino 32
sensor = DHT22(Pin(32))

# Lista de pinos da Barra de LEDs organizado pelas cores (verde, amarelo, vermelho)
# Verde: 21, 22, 23 - Amarelo: 13, 12, 14 - Vermelho: 27, 26, 25, 33
all_pins = [21, 22, 23, 13, 12, 14, 27, 26, 25, 33]
leds = [Pin(pin, Pin.OUT) for pin in all_pins]

def atualizar_barra_de_leds(temperatura):
    # Desliga todos os LEDs antes de atualizar o estado
    for led in leds:
        led.value(0)
        
    # Lógica de mapeamento para o freezer:
    # Ideal: -10°C ou menos
    # Crítico: 0°C ou mais
    qtd_leds_ligados = 0
    
    if temperatura <= -10:
        qtd_leds_ligados = 1 
    elif temperatura >= 0:
        qtd_leds_ligados = 10 
    else:
        # Calcula proporcionalmente quantos LEDs acender entre -9°C e -1°C
        qtd_leds_ligados = int((temperatura + 10) + 1)
        
    # Garante de forma segura que o valor fique entre 0 e 10
    qtd_leds_ligados = min(max(qtd_leds_ligados, 0), 10)
    
    # Liga a quantidade exata de LEDs calculada
    for i in range(qtd_leds_ligados):
        leds[i].value(1)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        
        print(f"Temperatura atual do Freezer: {temp}°C")
        atualizar_barra_de_leds(temp)
        
    except OSError as e:
        print("Falha ao ler o sensor DHT22!!!")
        
    time.sleep(1)
