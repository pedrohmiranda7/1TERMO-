# Plano de Ensino e Conteúdo Programático: Sistemas Operacionais

## 📋 1. Visão Geral da Disciplina
* **Curso:** Engenharia de Computação / Ciência da Computação / Análise de Sistemas
* **Disciplina:** Sistemas Operacionais (SO)
* **Carga Horária:** 60 Horas (Teórico-Prática)
* **Objetivo:** Compreender a estrutura, o funcionamento e os mecanismos de gerenciamento de recursos de hardware realizados pelo software de sistema.

---

## 🏗️ 2. Módulo I: Introdução e Arquitetura do SO

### 2.1 Conceitos Fundamentais
* **Papel do SO:** Intermediário entre o usuário/aplicações e o hardware do computador.
* **Modos de Operação do Processador:** 
    * **Modo Usuário:** Execução de aplicativos comuns com acesso restrito ao hardware.
    * **Modo Kernel (Supervisor):** Acesso total e irrestrito às instruções do processador e memória.
* **Chamadas de Sistema (System Calls):** Interface de programação que permite a um app solicitar serviços do Kernel.

### 2.2 Estruturas de Kernel
* **Monolítico:** Todas as funções do SO rodam no mesmo espaço de endereçamento do Kernel (Ex: Linux).
* **Microkernel:** Funções mínimas no Kernel; serviços rodam como processos em Modo Usuário (Ex: MINIX).
* **Híbrido:** Combinação de eficiência monolítica com modularidade (Ex: Windows NT).

---

## 🔄 3. Módulo II: Gerenciamento de Processos e Threads

### 3.1 Conceito de Processo
* **Definição:** Um programa em execução ativa contendo código, dados, registradores e pilha.
* **Bloco de Controle de Processo (PCB):** Estrutura de dados do Kernel que armazena o contexto do processo.
* **Estados do Processo:** Transições entre os estados *Novo*, *Pronto*, *Executando*, *Bloqueado* e *Terminado*.

### 3.2 Escalonamento da CPU (Scheduling)
* **Critérios:** Utilização da CPU, throughput, tempo de turnaround, tempo de resposta e tempo de espera.
* **Algoritmos Não-Preemptivos:** FIFO/FCFS (First-Come, First-Served) e SJF (Shortest Job First).
* **Algoritmos Preemptivos:** Round Robin (Alternância Circular por Quantum de tempo) e Prioridades.

### 3.3 Concorrência e Sincronização
* **Threads:** Unidades básicas de utilização da CPU dentro de um mesmo processo (compartilham memória).
* **Condição de Corrida:** Falha quando múltiplos processos modificam dados compartilhados simultaneamente.
* **Mecanismos de Exclusão Mútua:** Locks, Mutex e Semáforos para proteção de Regiões Críticas.
* **Deadlock (Impasses):** Situação onde processos ficam bloqueados perpetuamente esperando por recursos uns dos outros.

---

## 🧠 4. Módulo III: Gerenciamento de Memória

### 4.1 Memória Física e Alocação
* **Endereçamento Lógico vs Físico:** Unidade de Gerenciamento de Memória (MMU) traduz os endereços em tempo de execução.
* **Alocação Contígua:** Partições fixas e variáveis (Problemas de fragmentação interna e externa).

### 4.2 Memória Virtual
* **Paginamento:** Divisão da memória física em *Frames* (quadros) e da memória lógica em *Pages* (páginas).
* **Tabela de Páginas:** Mapeamento logístico para conversão de endereços de memória.
* **Falha de Página (Page Fault):** Interrupção gerada quando uma página requisitada não está carregada na RAM.
* **Algoritmos de Substituição de Página:** FIFO, LRU (Least Recently Used) e Ótimo.

---

## 💾 5. Módulo IV: Sistemas de Arquivos e Entrada/Saída (E/S)

### 5.1 Arquivos e Diretores
* **Conceito:** Abstração lógica de armazenamento criada pelo SO sobre os dispositivos físicos.
* **Métodos de Alocação de Espaço:** Alocação Contígua, Encadeada e Indexada (Ex: i-nodes no Linux).
* **Sistemas de Arquivos Comuns:** FAT32, NTFS, EXT4 e exFAT.

### 5.2 Subsistema de Entrada/Saída
* **Controladores de Dispositivos (Drivers):** Software que traduz comandos do SO para o hardware específico.
* **Métodos de Comunicação:** E/S Programada, Interrupções e DMA (Direct Memory Access - bypass da CPU).

---

## 📅 6. Cronograma Proposto de Aulas


| Aula | Conteúdo Teórico | Atividade Prática / Laboratório |
| :--- | :--- | :--- |
| **01** | Evolução Histórica e Objetivos dos Sistemas Operacionais | Exploração da interface de linha de comando (CLI) Bash/PowerShell |
| **02** | Arquitetura do Kernel, Modo Usuário vs Modo Kernel | Rastreamento de chamadas de sistema no Linux usando comando `strace` |
| **03** | Conceito de Processo e Criação de Processos | Criação e clonagem de processos em C com as funções `fork()` e `exec()` |
| **04** | Programação Concorrente com Threads | Implementação de Threads paralelas em C/C++ usando a biblioteca `pthread` |
| **05** | Simulação de Algoritmos de Escalonamento da CPU | Cálculo manual de tempos de espera com FIFO, SJF e Round Robin |
| **06** | Problema da Região Crítica e Condições de Corrida | Resolução de inconsistência de memória usando Mutex e Semáforos |
| **07** | Arquitetura de Memória e Paginação de Processos | Análise do mapa de memória de um processo ativo (`/proc/[pid]/maps`) |
| **08** | Algoritmos de Substituição de Páginas na Memória Virtual | Desenvolvimento de script em Python para simular faltas de página |
| **09** | Estrutura Interna de Sistemas de Arquivos e Permissões | Manipulação avançada de permissões e links físicos/simbólicos via terminal |
| **10** | Gerenciamento de Dispositivos e Sistemas Operacionais Modernos | Configuração e análise de logs do Kernel do sistema operacional (`dmesg`) |

---

## 📝 7. Critérios de Avaliação
* **Laboratórios Práticos (40%):** Atividades semanais de programação em C e manipulação de scripts em ambiente Unix/Linux.
* **Prova Teórica (40%):** Avaliação de conceitos de sincronização, escalonamento e paginação.
* **Trabalho Prático Integrador (20%):** Implementação de um mini-escalonador de processos simulado ou de um shell interativo personalizado em terminal.
