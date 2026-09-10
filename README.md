# Atividade Prática – Análise de Algoritmos de Ordenação

**Aluno:** Samuel Borges Cordeiro  
**Disciplina:** Estruturas de Dados  
**Instituição:** UDF  

## Objetivo

Comparar experimentalmente a quantidade de operações realizadas pelos algoritmos:

- Bubble Sort
- Insertion Sort
- Selection Sort
- Quick Sort

Os testes serão realizados com vetores de:

- 10 elementos
- 20 elementos
- 1.000 elementoss

Todos os algoritmos utilizarão cópias do mesmo vetor original em cada experimento.

## Critério de contagem

Durante os testes serão contabilizadas:

- comparações entre valores;
- trocas ou movimentações de elementos.

Os resultados serão utilizados para relacionar o tamanho da entrada, a quantidade de operações e a complexidade computacional dos algoritmos.
## Etapa 3 – Resultados

| Tamanho | Bubble Comparações | Bubble Trocas | Insertion Comparações | Insertion Mov. | Selection Comparações | Selection Trocas | Quick Comparações | Quick Mov. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 45 | 26 | 33 | 34 | 45 | 6 | 29 | 10 |
| 20 | 175 | 87 | 101 | 105 | 190 | 15 | 65 | 27 |
| 1000 | 498015 | 243076 | 244070 | 244070 | 499500 | 994 | 10234 | 4878 |

## Etapa 4 – Análise dos resultados

**a)** O Quick Sort realizou o menor número de comparações para 10 elementos, com 29 comparações.

**b)** O Selection Sort realizou menos trocas, com apenas 6 trocas para 10 elementos.

**c)** Sim. Para 20 elementos, o comportamento continuou semelhante. O Quick Sort continuou apresentando menos comparações.

**d)** Quando o vetor aumentou para 1.000 elementos, a quantidade de operações cresceu muito nos algoritmos Bubble Sort, Insertion Sort e Selection Sort. O Quick Sort apresentou um crescimento bem menor.

**e)** Não. Mesmo possuindo complexidade O(n²), os algoritmos não realizaram exatamente a mesma quantidade de operações. Com 1.000 elementos, o Bubble Sort realizou 498015 comparações, o Insertion Sort 244070 e o Selection Sort 499500.

**f)** O Bubble Sort e o Selection Sort apresentaram os maiores crescimentos no número de comparações. O Bubble Sort também realizou uma grande quantidade de trocas.

**g)** O Quick Sort apresentou um crescimento muito menor para o vetor aleatório. Com 1.000 elementos, realizou apenas 10234 comparações, enquanto Bubble e Selection ficaram próximos de 500 mil.

**h)** Sim. Os resultados estão de acordo com as complexidades teóricas. Bubble Sort, Insertion Sort e Selection Sort apresentaram comportamento próximo de O(n²), enquanto o Quick Sort apresentou desempenho próximo de O(n log n) para dados aleatórios.

**i)** Para ordenar milhares de pedidos, eu escolheria o Quick Sort, pois apresentou muito menos operações no experimento com 1.000 elementos.

## Desafio adicional

| Caso | Bubble C. | Bubble T. | Insertion C. | Insertion M. | Selection C. | Selection T. | Quick C. | Quick M. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Aleatório | 499200 | 242323 | 243316 | 243318 | 499500 | 995 | 10363 | 4931 |
| Ordenado | 999 | 0 | 999 | 0 | 499500 | 0 | 499500 | 0 |
| Inverso | 499500 | 499500 | 499500 | 500499 | 499500 | 500 | 499500 | 500 |

### Análise do desafio

A organização inicial dos dados interfere de forma diferente em cada algoritmo.

No Bubble Sort e no Insertion Sort, um vetor já ordenado reduz muito a quantidade de operações.

O Selection Sort continua realizando praticamente a mesma quantidade de comparações independentemente da organização inicial.

Nesta implementação do Quick Sort, foi utilizado o último elemento como pivô. Por isso, vetores já ordenados ou em ordem inversa representam casos ruins, aumentando bastante a quantidade de comparações.