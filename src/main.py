from machine import Pin, I2C, PWM
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep, ticks_ms, ticks_diff
from ssd1306 import SSD1306_I2C
import json

# Botão de silenciar o alarme junto com entrada com pull-up
botao = Pin(4, Pin.IN, Pin.PULL_UP)

# Configuração do Buzzer no pino 15
buzzer_pin = Pin(15, Pin.OUT)
buzzer = PWM(buzzer_pin)
buzzer.duty(0) # Garante que o alarme comece desligado

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

# Variáveis de controle para o alarme e leitura do sensor
ultimo_tempo_sensor = 0
esperando_conversao = False

ultimo_tempo_sirene = 0
estado_nota_aguda = True

ultimo_tempo_botao = 0
alarme_silenciado = False
temperatura_atual = -20  # Valor inicial seguro fictício

print("Temperatura") # expect text: 'Temperatura'

while True:
    try:
        tempo_atual = ticks_ms() # Captura o relógio do processador

        # Se apertado e passou 300ms do último clique (Debounce)
        if botao.value() == 0 and ticks_diff(tempo_atual, ultimo_tempo_botao) > 300:
            ultimo_tempo_botao = tempo_atual

            if temperatura_atual >= 0 and not alarme_silenciado:
                alarme_silenciado = True
                print("Alarme silenciado manualmente pelo operador.")

        # Pega a temperatura atual convertida a cada 750ms
        if enderecos_sensor:
            if not esperando_conversao:
                sensor.convert_temp()
                ultimo_tempo_sensor = tempo_atual
                esperando_conversao = True
            
            elif ticks_diff(tempo_atual, ultimo_tempo_sensor) >= 750:
                temperatura_atual = sensor.read_temp(enderecos_sensor[0])

                # Simula um payload JSON para um sistema IoT MQTT ou similar
                # Define o status em texto
                status_txt = "Ideal" if temperatura_atual <= -10 else "PERIGO" if temperatura_atual >= 0 else "Cuidado"

                # Cria um dicionário simulando um pacote de dados IoT
                payload = {
                    "device_id": "freezer_mamae_01",
                    "temperatura_c": temperatura_atual,
                    "status": status_txt,
                    "alerta_sonoro": temperatura_atual >= 0
                }
                
                # Imprime no formato JSON
                print(json.dumps(payload))

                atualizar_sistema(temperatura_atual)
                esperando_conversao = False 
            
                if temperatura_atual < 0:
                    alarme_silenciado = False
        else:
            # Tentativa de reconexão
            enderecos_sensor = sensor.scan()
            sleep(1) 

        # Toca apenas se estiver em perigo E ninguém tiver apertado o botão
        if temperatura_atual >= 0 and not alarme_silenciado:
            # Oscila o som a cada 200ms
            if ticks_diff(tempo_atual, ultimo_tempo_sirene) >= 200:
                ultimo_tempo_sirene = tempo_atual
                
                if estado_nota_aguda:
                    buzzer.freq(1200) # Tom alto
                else:
                    buzzer.freq(800)  # Tom baixo
                
                buzzer.duty(512)      # Liga o volume a 50%
                estado_nota_aguda = not estado_nota_aguda
        else:
            buzzer.duty(0) # Volume zero (silêncio)
            
    except Exception as e:
        print("Erro de execucao:", e)
        sleep(1) # Previne que um erro grave trave a placa rapidamente