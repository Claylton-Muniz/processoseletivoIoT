# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## 🏁 Passo 0 – Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo — eles fazem parte do processo de aprendizagem esperado.

---

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

> 📌 O GitHub será utilizado para:
> - Envio do seu projeto  
> - Versionamento do código  
> - Correção e validação automática via GitHub Actions  

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows
Baixe e instale o **Git Bash**:  
https://git-scm.com/downloads

### Linux / macOS
Verifique se o Git já está instalado:

```bash
git --version
```
> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## ⚙ Passo 1 – Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1️⃣ Fork do Repositório
No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />


Uma cópia do repositório será criada no seu perfil do GitHub

> 🔎 O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2️⃣ Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### 🔹 Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### 🔹 Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> ➡️ Todas as dependências serão instaladas automaticamente.

## 🔐 Passo 2 – Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: https://wokwi.com/dashboard/ci
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

>⚠️ Importante
- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## 🔒 Passo 3 – Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> ✔️ As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## 🧠 Passo 4 – Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### 📁 Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### 🛠 Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### 1️⃣ src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### 2️⃣ diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### 3️⃣ wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### 4️⃣ Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```
### ⚙ Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### 📌 Caso algo falhe:

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## 📊 Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## 📎 Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions  
2. Confirme que todos os arquivos obrigatórios estão presentes  
3. Copie o link do **seu repositório no GitHub**

📤 Envie o link conforme as orientações do processo seletivo na plataforma **Moodle**.

---

## 📝 Relatório do Candidato

### 👤 Identificação do Candidato

- **Nome completo:**  Claylton Demésio Muniz Silva
- **GitHub:**  [@Claylton-Muniz](https://github.com/Claylton-Muniz/)

---

## 1️⃣ Visão Geral da Solução

- **Objetivo do projeto**: Resolver um problema real e recorrente no varejo (especificamente projetado para um problema enfrentado na mercearia da minha mãe recentemente): a perda de perecíveis por falhas de refrigeração. O projeto entrega um sistema de monitoramento térmico preventivo, com uma arquitetura escalável que pode ser facilmente aplicada tanto em pequenos comércios quanto em grandes plantas industriais.

- **O que o sistema embarcado simulado faz**: Realiza a telemetria contínua de um freezer. O firmware processa os dados e define o estado do equipamento em três níveis: *Ideal* ($\le$ -10°C), *Atenção* (aquecendo) e *Crítico/Perigo* ($\ge$ 0°C). Pensando em escalabilidade para a Nuvem, o sistema possui uma arquitetura IoT-Ready, gerando e formatando payloads em JSON no terminal, simulando a estrutura exata que seria enviada a um Message Broker (como MQTT) em uma aplicação física.

- **Como o usuário interage**: O projeto conta com uma Interface Homem-Máquina (IHM) robusta para alertas locais:

  - **Visualização**: Uma barra de LEDs funciona como um termômetro visual rápido, apoiada por um Display OLED que exibe a temperatura exata e mensagens dinâmicas de ação (ex: alertas de risco e dicas de contenção).

  - **Alerta Sonoro e Controle**: Ao atingir a zona crítica, um buzzer é acionado para garantir a atenção imediata do operador. O usuário interage fisicamente através de um botão de reconhecimento (Acknowledge), que silencia o alarme sonoro enquanto o problema do freezer é investigado, enviando essa confirmação de manutenção também para o payload JSON.

---

## 2️⃣ Arquitetura do Sistema Embarcado

A arquitetura do firmware foi desenvolvida sob o paradigma de programação não-bloqueante, simulando o comportamento de um scheduler cooperativo simples. Isso garante que o microcontrolador nunca congele sua execução, permitindo o gerenciamento de múltiplas tarefas simultâneas (como ler sensores, atualizar o display e pulsar o alarme).

- **Fluxo Principal (main.py)**: O ciclo de vida do software é estruturado em duas fases distintas:

  1. **Setup**: Configuração primária dos barramentos de comunicação (I2C para o Display OLED e 1-Wire para o DS18B20) e instanciação dos pinos GPIO (Barra de LEDs, Botão com Pull-Up interno e Buzzer via PWM).

  2. **Loop**: O sistema opera em um ciclo infinito não-bloqueante. Utilizando a função *ticks_ms()*, o microcontrolador monitora o tempo de processamento contínua e simultaneamente, executando blocos de código apenas quando seus intervalos específicos são atingidos. Para garantir precisão e confiabilidade em nível industrial, a lógica foi desenhada como uma cascata de eventos, onde cada ação engatilha uma resposta física no hardware:

      - **O Gatilho**: O ciclo inicia solicitando dados ao sensor DS18B20. Dada a sua alta precisão, o componente exige 750ms para a conversão analógico-digital. Graças à arquitetura não-bloqueante, o código apenas agenda a leitura e continua sua execução, garantindo que o sistema (como o botão de reconhecimento/silêncio) permaneça 100% responsivo durante essa espera.

      - **O Processamento de Dados**: Após o intervalo de conversão, a temperatura é resgatada e injetada na função *atualizar_sistema()*. O firmware avalia o valor bruto contra os limites de segurança pré-estabelecidos: Ideal (<= -10°C) e Crítico (>= 0°C), determinando o estado atual da máquina.

      - **A Resposta na IHM**: Baseado no estado calculado, as saídas são acionadas. A quantidade exata de LEDs é acesa e o Display OLED é atualizado dinamicamente. Caso o limite crítico (0°C) seja ultrapassado, o alarme sonoro (Buzzer) é ativado e o display passa a exibir instruções de ação direta ("Salve a comida!"), visando orientar a tomada de decisão do funcionário sob pressão.

      - **Saída de Dados**: Concluindo o ciclo bem-sucedido, os dados de telemetria e o status dos alarmes são empacotados em um objeto JSON e imprimindo. Essa formatação padronizada foi implementada prevendo uma futura escalabilidade para a Nuvem (ex: via protocolo MQTT), permitindo o monitoramento remoto do freezer em tempo real através de dashboards ou dispositivos móveis.

- **Estrutura de Estados e Temporizações**: Para evitar o uso de *time.sleep()* (que paralisaria a leitura do botão e os avisos), o projeto utiliza variáveis de estado e temporizadores assíncronos (*ticks_diff*):

  - **Máquina de Estados do Sensor (750ms)**: Como o sensor DS18B20 exige tempo físico para realizar a conversão térmica de alta precisão, o sistema envia o comando de conversão e continua rodando. Apenas após 750ms, ele resgata o valor lido.
  
  - **Debounce via Software (300ms)**: Uma trava de tempo de 300ms foi implementada na leitura do botão para evitar o efeito "bouncing" (ruído mecânico que gera leituras múltiplas e incorretas de um único clique).
  
  - **Oscilador da Sirene (200ms)**: Alterna a frequência do sinal PWM do Buzzer entre 1200Hz e 800Hz a cada 200ms, criando um som contínuo e chamativo de alerta de emergência.
  
  - **Reset de Estados**: Variáveis como *alarme_silenciado* (booleana) controlam o fluxo lógico. Se a temperatura retorna a um nível seguro ($<$ 0°C), o estado de alarme é reiniciado automaticamente para a próxima ocorrência.

- **Interação entre os Componentes**:

  ```
  [Loop Assíncrono Principal]
      │
      ├─► 1. (Botão Push) ────── Pressionado? ──► Confirma evento e silencia Buzzer
      │
      ├─► 2. (Sensor DS18B20) ── Passou 750ms? ─► Lê Temperatura ─► Transmite Payload JSON (Serial)
      │                                                │
      │                                                ├──► Enche/Esvazia Barra de LEDs
      │                                                └──► Escreve alertas no Display OLED
      │
      └─► 3. (Buzzer PWM) ────── Perigo Ativo E Não Silenciado? 
                                                       │
                                                       └─► Alterna tons sonoros a cada 200ms
  ```

---

## 3️⃣ Componentes Utilizados na Simulação

- **Placa de Desenvolvimento**: Quem atua como o cérebro do sistema é o ESP32 como definido no próprio projeto antes do fork, executando o firmware MicroPython, gerenciando I/O e temporizadores).

- **Sensor de Temperatura**: DS18B20 (Protocolo 1-Wire. Escolhido estrategicamente por ser encapsulado e à prova d'água em cenários reais, sendo o padrão industrial para medição em freezers e câmaras frias).

- **Display**: OLED SSD1306 128x64 (Protocolo I2C. Responsável pela Interface Homem-Máquina visual, exibindo a temperatura em graus Celsius e mensagens de ação).

- **Sinalização Visual**: Barra de LEDs (10 segmentos) (Mapeada via GPIOs individuais. Atua como um termômetro visual rápido, indo do verde ao vermelho conforme a temperatura sobe).

- **Sinalização Sonora**: Buzzer Piezoelétrico (Controlado via PWM. Acionado como alarme crítico quando a temperatura atinge níveis de perda de estoque - 0°C).

- **Interação Física**: Push Button (Botão) (Conectado com resistor de Pull-Up interno. Usado pelo operador para reconhecer a falha e silenciar temporariamente a sirene de alerta).

- **Componentes Passivos**: Resistores de 220Ω (para limitação de corrente nos LEDs) e 4.7kΩ (para o barramento 1-Wire do sensor de temperatura).

---

## 4️⃣ Decisões Técnicas Relevantes

Durante o desenvolvimento do firmware e da infraestrutura, algumas decisões arquiteturais foram tomadas para garantir que o protótipo refletisse um produto robusto:

- **Organização do código**: O projeto foi estruturado com foco em modularidade, legibilidade e fácil manutenção. A biblioteca de controle do display (ssd1306.py) foi completamente isolada do arquivo de execução principal (main.py). O fluxo de execução foi dividido estritamente entre a fase de inicialização estática (Setup de GPIOs e barramentos) e o Loop, evitando a poluição do escopo global.

- **Uso de funções, estados e constantes**: A regra de negócio principal — que calcula os limites de temperatura e atua sobre os LEDs e o display — foi extraída e encapsulada na função *atualizar_sistema(temperatura)*. Isso manteve o loop principal enxuto. O controle de fluxo é regido por variáveis de estado precisas (como a booleana *alarme_silenciado* e *esperando_conversao*). Para os atuadores, os pinos da barra de LEDs foram agrupados em uma lista constante (*all_pins*), otimizando o acionamento em massa através de laços de repetição de forma escalável.

- **Estratégias para temporização e controle lógico**: uso de *time.sleep()* foi terminantemente evitado. Toda a estratégia de temporização foi construída usando o cálculo de diferença de tempo (*ticks_diff()*) sobre o relógio do processador (*ticks_ms()*). Esse controle lógico não-bloqueante permite gerenciar simultaneamente a janela de 750ms do sensor térmico, a oscilação de 200ms do alarme e o filtro de debounce de 300ms do botão, mantendo o sistema 100% responsivo a ações do usuário.

- **Substituição do Sensor de Temperatura**: O uso de sensores comuns (como o DHT22) foi descartado, pois a umidade e o gelo de um freezer real os destruiriam. Optou-se pelo DS18B20 (1-Wire), encapsulado em aço inox e selado contra água, que é o padrão da indústria de refrigeração comercial.

- **Saída Orientada a Dados (JSON)**: Em vez de imprimir textos soltos no terminal (ex: "A temperatura é X"), o sistema foi desenhado para gerar payloads em formato JSON. Essa decisão técnica prepara o terreno para uma integração fácil com plataformas de Nuvem (AWS IoT, GCP) via MQTT no futuro, separando a camada de sensoriamento da camada de aplicação.

- **Resolução de Conflitos no Docker**: Para manter a modularização do código (separando a biblioteca *ssd1306.py* do *main.py*), foi necessário realizar um troubleshooting no arquivo *Dockerfile* do pipeline. A instrução de cópia foi alterada de (COPY src/main.py /main.py) para (COPY src/*.py /), garantindo que o build da imagem montasse o filesystem (fs.bin) com todos os arquivos dependentes, permitindo que a simulação rodasse perfeitamente no GitHub Actions.

---

## 5️⃣ Resultados Obtidos

O protótipo final atingiu com êxito todos os objetivos propostos, comportando-se como um sistema de monitoramento industrial estável, responsivo e pronto para escalabilidade.

- **O que funciona corretamente**: A arquitetura assíncrona operou perfeitamente. O sistema lê a temperatura do sensor DS18B20 rigorosamente a cada 750ms, atualizando a barra de LEDs e o Display OLED em tempo real, e acionando o Buzzer (PWM) nos momentos de violação térmica. Crucialmente, o botão de reconhecimento (Acknowledge) funciona de forma instantânea (protegido por debounce de software), permitindo que o operador silencie a sirene de emergência sem que o microcontrolador congele, interrompa ou atrase as demais rotinas de leitura e emissão de dados.

- **Quais requisitos foram atendidos**: Todos os critérios de software e infraestrutura foram plenamente satisfeitos. A lógica de firmware (leitura de sensores e atuação não-bloqueante via máquina de estados) foi concluída; o diagrama de hardware reflete a solução com precisão; e os testes automatizados de CI/CD (GitHub Actions) foram aprovados, validando a estabilidade do repositório em ambientes de integração contínua.

- **Resultado observado na simulação do Wokwi**: Ao iniciar a simulação, o ESP32 realiza o setup e imprime a string inicial de inicialização, o que garante a aprovação rápida no robô de testes do pipeline. Ao manipular o slider de temperatura do DS18B20 manualmente na interface, observa-se a transição imediata dos três estados (Ideal $\rightarrow$ Atenção $\rightarrow$ Perigo) refletida perfeitamente na IHM (LEDs e OLED). O terminal Serial exibe continuamente o fluxo de pacotes JSON, comprovando que o dispositivo está extraindo dados consistentes.

---

## 6️⃣ Comentários Adicionais (Opcional)

O maior obstáculo técnico não foi o código MicroPython em si, mas a integração do projeto modularizado com o pipeline de testes automatizados do GitHub Actions. O simulador via Wokwi CLI estava falhando (Timeout) e o ambiente Docker original não empacotava arquivos secundários (como a biblioteca do OLED). Resolver isso exigiu investigar a fundo o funcionamento da ferramenta mklittlefs, reescrever as regras de build no Dockerfile e ajustar as variáveis de ambiente (CI_EXPECT_TEXT) no workflow do GitHub.

### Melhorias que eu faria com mais tempo

- **Refatoração Orientada a Objetos**: Migraria a lógica principal para classes específicas (ex: criar uma classe FreezerMonitor e uma classe Alarme), limpando o arquivo main.py e deixando o código ainda mais modular.

- **Conectividade Real**: Substituiria o print do JSON pela implementação da biblioteca umqtt.simple, conectando o ESP32 a uma rede Wi-Fi e publicando os payloads diretamente em um broker MQTT gratuito (como o HiveMQ ou Mosquitto).

- **Timestamps Locais**: Adicionaria a sincronização de tempo via NTP (Network Time Protocol) ou um módulo RTC para adicionar carimbos de data/hora precisos dentro do JSON gerado, o que é fundamental para banco de dados de séries temporais industriais.

---
