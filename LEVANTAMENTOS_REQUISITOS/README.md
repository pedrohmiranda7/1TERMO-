# Ementa e Conteúdo Programático: Engenharia e Levantamento de Requisitos

## 📋 1. Visão Geral da Disciplina
* **Curso:** Engenharia de Software / Análise e Desenvolvimento de Sistemas
* **Disciplina:** Engenharia de Requisitos
* **Carga Horária:** 40 Horas
* **Objetivo:** Capacitar o aluno a descobrir, analisar, documentar e validar as necessidades dos stakeholders para o desenvolvimento de softwares de alta qualidade.

---

## 🔍 2. Módulo I: Classificação de Requisitos

### 2.1 Requisitos Funcionais (RF)
* **Conceito:** Definem as ações, comportamentos e funções específicas que o sistema deve executar.
* **Foco:** O que o sistema deve fazer (Entradas, processamentos e saídas).
* **Exemplos Práticos:**
    * **RF01:** O sistema deve permitir o cadastro de novos usuários com validação de CPF.
    * **RF02:** O sistema deve enviar um e-mail de confirmação após a finalização de uma compra.
    * **RF03:** O usuário deve conseguir exportar o relatório de vendas em formato PDF.

### 2.2 Requisitos Não Funcionais (RNF)
* **Conceito:** Definem as qualidades, restrições, premissas e características globais do sistema.
* **Foco:** Como o sistema deve realizar suas funções (Atributos de qualidade).
* **Categorias Principais:**
    * **Desempenho:** O sistema deve processar as buscas em menos de 2 segundos.
    * **Segurança:** Todas as senhas devem ser criptografadas utilizando o algoritmo SHA-256.
    * **Disponibilidade:** O sistema deve manter uma taxa de disponibilidade de 99,9% (Uptime).
    * **Usabilidade:** A interface deve ser responsiva e adaptável a dispositivos móveis.

---

## 🗣️ 3. Módulo II: Técnicas de Elicitação de Requisitos

### 3.1 Entrevistas
* **Tipos:** Estruturadas (roteiro fixo), Não Estruturadas (conversa livre) e Semi-estruturadas.
* **Aplicação:** Coleta aprofundada de informações diretamente com tomadores de decisão ou especialistas do negócio.
* **Boas Práticas:** Evitar perguntas indutivas, registrar o áudio (com autorização) e documentar as respostas imediatamente.

### 3.2 Brainstorming
* **Conceito:** Sessões dinâmicas em grupo para geração livre de ideias sem julgamentos prévios.
* **Aplicação:** Fase inicial do projeto para descobrir funcionalidades inovadoras ou resolver problemas complexos.
* **Regras de Ouro:** Foco em quantidade de ideias, fomento a visões alternativas e registro visual de todos os insights.

### 3.3 Prototipagem
* **Prototipagem de Baixa Fidelidade:** Desenhos em papel (Wireframes) para validação rápida de fluxos de telas.
* **Prototipagem de Alta Fidelidade:** Modelos interativos (Figma, Adobe XD) para validação visual e de experiência do usuário (UX).
* **Vantagem:** Reduz o desalinhamento de expectativas antes do início do desenvolvimento do código.

---

## 📊 4. Módulo III: Modelagem e Diagramas de Requisitos

### 4.1 Diagrama de Casos de Uso (UML)
* **Atores:** Entidades externas (usuários ou outros sistemas) que interagem com o software.
* **Casos de Uso:** Funcionalidades representadas por elipses.
* **Relacionamentos:** `<<include>>` (obrigatoriedade) e `<<extend>>` (opcionalidade).

