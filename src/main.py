from machine import Pin, I2C
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep, sleep_ms
from ssd1306 import SSD1306_I2C

# Configuração do Buzzer no pino 15
buzzer = Pin(15, Pin.OUT)
buzzer.value(0) # Garante que o alarme comece desligado

# Configuração do Sensor DS18B20 no pino 32
pino_dados = Pin(32)
sensor = DS18X20(OneWire(pino_dados))
enderecos_sensor = sensor.scan()

# Configuração do I2C para o display OLED
i2c = I2C(0, scl=Pin(18), sda=Pin(19)) 
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# Lista de pinos da Barra de LEDs organizado pelas cores
# Verde: 21, 22, 23 - Amarelo: 13, 12, 14 - Vermelho: 27, 26, 25, 33
all_pins = [21, 22, 23, 13, 12, 14, 27, 26, 25, 33]
leds = [Pin(pin, Pin.OUT) for pin in all_pins]

def atualizar_sistema(temperatura):
    # Desliga todos os LEDs antes de atualizar o estado
    for led in leds:
        led.value(0)
        
    # Lógica do Alarme Sonoro
    if temperatura >= 0:
        buzzer.value(1) # Ativa o som
    else:
        buzzer.value(0) # Desativa o som
        
    # Lógica de mapeamento para os LEDs do freezer
    qtd_leds_ligados = 0
    
    if temperatura <= -10:
        qtd_leds_ligados = 1 
    elif temperatura >= 0:
        qtd_leds_ligados = 10 
    else:
        # Calcula quantos LEDs acender entre -9°C e -1°C
        qtd_leds_ligados = min(int((temperatura + 10) + 1), 9)
    
    # Liga os LEDs calculados
    for i in range(qtd_leds_ligados):
        leds[i].value(1)

    # Atualiza o Display OLED
    oled.fill(0)
    oled.text(f'Temp: {temperatura:.1f}C', 0, 0)

    if temperatura <= -10:
        oled.text('Status: Ideal', 0, 12)
    elif temperatura >= 0:
        oled.text('Status: PERIGO!', 0, 12)
        oled.text('Estado de risco!', 0, 24)
        oled.text('Salve a comida!', 0, 36)
    else:
        oled.text('Status: Cuidado', 0, 12)
        oled.text('Temp. subindo!', 0, 24)
        oled.text('Fique de olho.', 0, 36)

    oled.show()

print("Temperatura") # expect text: 'Temperatura'

while True:
    try:
        if enderecos_sensor:
            # O DS18B20 exige um comando de conversão antes da leitura
            sensor.convert_temp()
            
            # O sensor precisa de pelo menos 750ms para processar a temperatura
            sleep_ms(750) 
            
            # Lê a temperatura do primeiro sensor encontrado na rede One-Wire
            temp = sensor.read_temp(enderecos_sensor[0])
            
            print(f"Temperatura atual do Freezer: {temp:.2f}°C")
            atualizar_sistema(temp)
            
        else:
            print("Sensor não detectado. Tentando buscar novamente...")
            enderecos_sensor = sensor.scan()
            sleep(2)
            
    except Exception as e:
        print("Falha ao ler o sensor DS18B20:", e)
        sleep(1)