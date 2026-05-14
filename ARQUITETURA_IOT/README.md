# Plano de Ensino e Conteúdo Programático: Arquitetura IoT

## 📋 1. Visão Geral da Disciplina
* **Curso:** Engenharia de Computação / Sistemas de Informação
* **Disciplina:** Arquitetura de Internet das Coisas (IoT)
* **Carga Horária:** 60 Horas (Teórico-Prática)
* **Pré-requisitos:** Algoritmos, Circuitos Digitais básicos.

### Objetivo Geral
Capacitar o aluno a projetar, desenvolver e integrar sistemas IoT fim-a-fim, cobrindo desde a captura de dados por sensores no ecossistema Arduino (Edge), passando pela programação em C++ e Python, até o envio de telemetria para Gateways.

---

## 🛠️ 2. Módulo I: Hardware e Ecossistema Arduino (A Camada Edge)

### 1.1 Introdução à Computação Física
* **Microcontrolador vs Microprocessador:** Diferenças de arquitetura (Harvard vs Von Neumann), consumo energético, clock e custo.
* **Ecossistema Arduino:** O ecossistema de hardware livre, pinagens e evolução das placas.
* **Anatomia do Arduino Uno:** Detalhamento do chip ATmega328P, memórias Flash, SRAM e EEPROM.

### 1.2 Interfaces de Entrada e Saída (GPIO)
* **Pinos Digitais:** Configuração de entrada (`INPUT`, `INPUT_PULLUP`) e saída (`OUTPUT`).
* **Pinos Analógicos:** O funcionamento do Conversor Analógico-Digital (ADC) de 10 bits.
* **Modulação por Largura de Pulso (PWM):** Controle de potência analógica simulada em saídas digitais.

### 1.3 Protocolos de Comunicação Inter-Chips
* **UART (Universal Asynchronous Receiver-Transmitter):** Comunicação serial assíncrona ponto a ponto (Pinos RX/TX).
* **I2C (Inter-Integrated Circuit):** Barramento síncrono a dois fios (SDA/SCL) para múltiplos dispositivos.
* **SPI (Serial Peripheral Interface):** Comunicação síncrona a quatro fios (MISO, MOSI, SCK, SS) de alta velocidade.

### 1.4 Sensores e Atuadores no Contexto IoT
* **Sensores Comuns:** Leitura de temperatura/umidade (DHT11/DHT22), luminosidade (LDR) e presença (PIR).
* **Atuadores Comuns:** Controle de relés, servomotores e sinalizadores (LEDs/Buzzers).

---

## 💻 3. Módulo II: Desenvolvimento de Firmware com C/C++

### 2.1 Estrutura Fundamental do Firmware Arduino (.ino)
* **Ciclo de Vida:** O papel das funções nativas de inicialização e execução contínua.

```cpp
// Executado uma única vez na inicialização ou reset do hardware
void setup() {
  pinMode(13, OUTPUT);      // Configura o pino do LED integrado como saída
  pinMode(A0, INPUT);       // Configura o pino A0 para leitura de sensor
  Serial.begin(9600);       // Inicializa a comunicação serial a 9600 bps
}

// Executado em loop infinito de forma sequencial
void loop() {
  int valorSensor = analogRead(A0);       // Leitura do sensor analógico
  Serial.println(valorSensor);            // Envia o dado via UART
  
  digitalWrite(13, HIGH);                 // Liga o LED
  delay(1000);                            // Bloqueio temporário (1 segundo)
  digitalWrite(13, LOW);                  // Desliga o LED
  delay(1000);                            // Bloqueio temporário (1 segundo)
}
```

### 2.2 Otimização de Código para Sistemas Embarcados
* **Tipagem Estrita de Dados:** Substituição do tipo genérico `int` por tipos de tamanho fixo (`int8_t`, `uint8_t`, `uint16_t`) para economizar memória SRAM.
* **Funções Não-Bloqueantes:** Substituição da função `delay()` pelo controle de tempo baseado no timer interno `millis()`.
* **Máquinas de Estados Finitos (FSM):** Estruturação do loop principal utilizando a estrutura `switch/case` para alternar estados do dispositivo de forma eficiente.

### 2.3 Interrupções por Hardware (ISRs)
* **Conceito:** Desvio do fluxo principal do código por eventos externos assíncronos.
* **Implementação:** Uso da função `attachInterrupt()` mapeada em pinos específicos do Arduino.

---

## 🐍 4. Módulo III: Camada de Gateway e Integração com Python

### 3.1 O Papel do Python na Arquitetura IoT
* **Processamento de Borda (Edge Analytics):** Filtragem e validação de dados antes do envio para servidores Cloud.
* **Gerenciamento de Logs:** Armazenamento local de históricos de telemetria em arquivos CSV ou bancos de dados leves (SQLite).

### 3.2 Script de Captura de Dados Serial (Python)
* **Biblioteca PySerial:** Leitura de streams de dados brutos trafegados pela porta USB/Serial do computador/gateway.

```python
import serial
import time

# Configuração da porta de comunicação (Ajustar 'COM3' para Windows ou '/dev/ttyUSB0' para Linux)
porta_serial = '/dev/ttyACM0'
velocidade = 9600

try:
    arduino = serial.Serial(porta_serial, velocidade, timeout=1)
    time.sleep(2)  # Tempo necessário para o Arduino reiniciar após a abertura da conexão
    print(f"Conexão estabelecida com sucesso em: {porta_serial}")
    
    while True:
        if arduino.in_waiting > 0:
            # Lê a linha de dados, decodifica de bytes para string e remove quebras de linha
            linha_bruta = arduino.readline()
            dados_texto = linha_bruta.decode('utf-8').strip()
            
            # Validação simples do dado recebido
            if dados_texto.isdigit():
                leitura_sensor = int(dados_texto)
                print(f"Telemetria Recebida -> Sensor: {leitura_sensor}")
                
except serial.SerialException as e:
    print(f"Erro de conexão serial: {e}")
except KeyboardInterrupt:
    print("\nMonitoramento encerrado pelo usuário.")
finally:
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()
        print("Porta serial fechada.")
```

### 3.3 Comunicação em Redes IoT com Python
* **Protocolo MQTT:** Publicação de dados de telemetria usando a biblioteca `paho-mqtt` em corretores (Brokers) como Mosquitto ou HiveMQ.
* **Protocolo HTTP:** Envio de dados via requisições do tipo `POST` utilizando a biblioteca `requests` para APIs RESTful de plataformas IoT.

---

## 📊 5. Cronograma de Aulas Sugerido


| Aula | Conteúdo Prático / Teórico | Tecnologia Foco |
| :--- | :--- | :--- |
| **01** | Introdução à Arquitetura IoT (Sensores, Redes e Gateways) | Conceitos Gerais |
| **02** | Arquitetura do Hardware Arduino e Configuração da IDE | Arduino & GPIO |
| **03** | Entradas/Saídas Analógicas, Digitais e Modulação PWM | C++ (Firmware) |
| **04** | Protocolos de Comunicação Interna (UART, I2C, SPI) | Hardware Arduino |
| **05** | Temporização Eficiente com Millis e Interrupções | C++ Avançado |
| **06** | Manipulação de Strings e Formatação de Dados para Envio | C++ Avançado |
| **07** | Configuração de Ambiente Python e Manipulação da Porta Serial | Python & PySerial |
| **08** | Parseamento, Filtragem e Tratamento de Exceções de Dados | Python |
| **09** | Armazenamento de Dados de Telemetria Local (CSV/SQL) | Python |
| **10** | Integração Fim-a-Fim: Arduino enviando dados para Gateway Python | C++ e Python |

---

## 📝 6. Metodologia de Avaliação e Projetos
* **Mini-Projetos de Bancada (40%):** Práticas de laboratório semanais envolvendo circuitos e códigos simples.
* **Projeto Integrador Final (60%):** Desenvolvimento de uma estação meteorológica ou sistema de automação residencial. O projeto deve obrigatoriamente coletar dados via Arduino (C++), transmitir via Serial para um Gateway (Python) e disparar alertas textuais ou visuais em tela.
