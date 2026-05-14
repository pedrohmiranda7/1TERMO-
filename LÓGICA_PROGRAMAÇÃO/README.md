# Plano de Ensino e Conteúdo Programático: Lógica e Programação

## 📋 1. Visão Geral da Disciplina
* **Curso:** Computação / Engenharia / Análise de Sistemas
* **Disciplina:** Lógica de Programação e Algoritmos
* **Carga Horária:** 80 Horas (Teórico-Prática)
* **Objetivo:** Desenvolver o raciocínio lógico estruturado para a resolução de problemas computacionais e codificação em linguagem de programação.

---

## 🧩 2. Módulo I: Conceitos Básicos e Lógica Estruturada

### 2.1 O que é um Algoritmo?
* **Definição:** Sequência finita de passos lógicos e não ambíguos para resolver um problema.
* **Formas de Representação:**
    * **Descrição Narrativa:** Texto em linguagem natural (passo a passo de uma receita).
    * **Fluxograma:** Representação gráfica universal utilizando blocos geométricos padrão.
    * **Pseudocódigo (Portugol):** Linguagem intermediária estruturada próxima ao código real.

### 2.2 Anatomia de um Algoritmo (Entrada, Processamento e Saída)
* **Variáveis e Constantes:** Espaços de memória para armazenamento temporário de informações.
* **Tipos de Dados Primitivos:**
    * **Inteiro:** Números sem casas decimais (`10`, `-5`, `0`).
    * **Real / Float:** Números com ponto flutuante (`1.75`, `-10.5`).
    * **Caractere / String:** Texto ou símbolos (`"Olá Mundo"`, `"A"`).
    * **Lógico / Booleano:** Estados binários verdade/falso (`True`, `False`).
* **Operadores Aritméticos:** Adição (`+`), Subtração (`-`), Multiplicação (`*`), Divisão (`/`) e Resto (`%` ou `Mod`).

---

## 🔀 3. Módulo II: Estruturas de Controle de Fluxo

### 3.1 Estruturas Condicionais (Tomada de Decisão)
* **Condicional Simples e Composta (`SE / SENÃO`):** Desvia o fluxo do código com base em um teste lógico.
* **Operadores Relacionais:** Maior que (`>`), Menor que (`<`), Igual (`==`) e Diferente (`!=`).
* **Operadores Lógicos:** Conjunção (`E / AND`), Disjunção (`OU / OR`) e Negação (`NÃO / NOT`).

```python
# Exemplo de Condicional Composta em Python
idade = 18

if idade >= 18:
    print("Acesso liberado: Maior de idade.")
else:
    print("Acesso negado: Menor de idade.")
```

### 3.2 Estruturas de Repetição (Loops / Laços)
* **Laço Contado (`PARA / FOR`):** Utilizado quando o número exato de repetições é conhecido previamente.
* **Laço Condicional (`ENQUANTO / WHILE`):** Executa o bloco de código repetidamente enquanto uma condição for verdadeira.

```python
# Exemplo de Laço Contado (FOR) para exibir uma tabuada
numero = 5
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

---

## 🗄️ 4. Módulo III: Estruturas de Dados Básicas e Modularização

### 4.1 Vetores e Matrizes (Arrays)
* **Vetores (Unidimensionais):** Listas indexadas de elementos de um mesmo tipo de dado.
* **Matrizes (Bidimensionais):** Tabelas organizadas em linhas e colunas para armazenamento de dados complexos.

### 4.2 Funções e Procedimentos (Modularização)
* **Conceito:** Divisão de um código grande em blocos menores, isolados e reaproveitáveis.
* **Parâmetros e Retorno:** Variáveis de entrada passadas para a função e o resultado retornado após o processamento.

```python
# Exemplo de Função com Parâmetros e Retorno
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

# Chamada da função
resultado_final = calcular_media(7.5, 8.5)
print(f"Média Final: {resultado_final}")
```

---

## 📅 5. Cronograma Proposto de Aulas



| Aula | Conteúdo Teórico | Atividade Prática / Laboratório |
| :--- | :--- | :--- |
| **01** | Pensamento Computacional e Lógica no Cotidiano | Criação de algoritmos em papel (Narrativos) |
| **02** | Variáveis, Constantes e Tipos de Dados Primitivos | Exercício de declaração e atribuição de variáveis |
| **03** | Operadores Aritméticos e Expressões Matemáticas | Construção de fórmulas computacionais básicas |
| **04** | Estrutura Condicional Simples e Composta (`IF/ELSE`) | Algoritmo de validação de médias e aprovação |
| **05** | Operadores Lógicos Complexos e Condicionais Alinhadas | Criação de sistemas de triagem por múltiplos critérios |
| **06** | Estruturas de Repetição Condicional (`WHILE`) | Validação de dados de entrada com repetição |
| **07** | Estruturas de Repetição Contada (`FOR`) | Algoritmos de somatório, contagem e tabuadas |
| **08** | Introdução a Vetores (Listas / Arrays) | Armazenamento e leitura de listas de nomes e notas |
| **09** | Manipulação de Vetores (Busca e Filtragem) | Localizar o maior e o menor valor dentro de uma lista |
| **10** | Modularização: Criação e uso de Funções | Isolamento de regras de negócio em funções isoladas |

---

## 📝 6. Diretrizes de Avaliação
* **Listas de Exercícios (30%):** Resolução de problemas semanais de lógica para fixação de sintaxe.
* **Desafios de Programação (40%):** Testes práticos individuais no laboratório com computadores desligados da internet.
* **Projeto de Bloco (30%):** Desenvolvimento de um sistema textual interativo (Ex: Mini-caixa eletrônico, Jogo da Velha via terminal ou Sistema de Cadastro escolar).
