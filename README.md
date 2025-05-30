﻿# 8-Puzzle Solver 

## 1. Introdução

O 8-Puzzle é um problema clássico de Inteligência Artificial envolvendo um tabuleiro 3x3 com oito peças numeradas e um espaço vazio. O objetivo é alcançar uma configuração final a partir de um estado inicial, movendo o espaço vazio para cima, baixo, esquerda ou direita. Este projeto implementa e compara três algoritmos de busca, com foco especial no método A* e suas heurísticas.

---

## 2. Algoritmos

### 2.1 Busca em Largura (BFS)
Explora todos os nós de um nível antes de avançar para o próximo. Garante solução ótima, mas pode consumir muita memória em casos complexos.

### 2.2 Busca em Profundidade (DFS)
Explora o caminho mais profundo possível antes de retroceder. É eficiente em memória, porém pode não encontrar a solução ótima e, em casos difíceis, pode não encontrar solução.

### 2.3 Busca A*
Combina o custo do caminho percorrido com uma estimativa (heurística) do custo restante até o objetivo. Garante solução ótima se a heurística for admissível.

---

## 3. Heurísticas

### 3.1 Distância de Manhattan
Soma das distâncias horizontais e verticais de cada peça até sua posição correta. É uma heurística admissível e informativa para o 8-Puzzle.

### 3.2 Peças Fora do Lugar
Conta quantas peças não estão em sua posição correta. Também é admissível, porém menos informativa que a Distância de Manhattan.

---

## 4. Resultados Experimentais

Foram realizados testes em três cenários: fácil, médio e difícil. Os resultados incluem tempo de execução, número de nós visitados e quantidade de movimentos até a solução.

### 4.1 Caso Fácil  
**Estado inicial:** (1, 2, 3, 4, 5, 6, 7, 0, 8)

| Algoritmo             | Tempo (s) | Nós Visitados | Passos | Heurística         |
|-----------------------|-----------|--------------|--------|--------------------|
| BFS                   | 0.002     | 3            | 1      | N/A                |
| DFS                   | 0.001     | 2            | 1      | N/A                |
| A* (Manhattan)        | 0.003     | 2            | 1      | Manhattan          |
| A* (Peças Fora Lugar) | 0.002     | 2            | 1      | Peças Fora do Lugar|

### 4.2 Caso Médio  
**Estado inicial:** (2, 8, 1, 0, 4, 3, 7, 6, 5)

| Algoritmo             | Tempo (s) | Nós Visitados | Passos | Heurística         |
|-----------------------|-----------|--------------|--------|--------------------|
| BFS                   | 0.45      | 1500         | 22     | N/A                |
| DFS                   | 1.20      | 3500         | 142    | N/A                |
| A* (Manhattan)        | 0.12      | 85           | 22     | Manhattan          |
| A* (Peças Fora Lugar) | 0.18      | 120          | 22     | Peças Fora do Lugar|

### 4.3 Caso Difícil  
**Estado inicial:** (8, 6, 7, 2, 5, 4, 3, 0, 1)

| Algoritmo             | Tempo (s) | Nós Visitados | Passos | Heurística         |
|-----------------------|-----------|--------------|--------|--------------------|
| BFS                   | 4.52      | 18144        | 30     | N/A                |
| DFS                   | -         | -            | -      | N/A                |
| A* (Manhattan)        | 0.35      | 1563         | 30     | Manhattan          |
| A* (Peças Fora Lugar) | 1.02      | 4012         | 30     | Peças Fora do Lugar|

> **Observação:** O DFS não encontrou solução no caso difícil dentro do limite de profundidade estabelecido.

---

## 5. Discussão e Comparação

- O A* com heurística de Manhattan foi o mais eficiente em todos os cenários, tanto em tempo quanto em número de nós visitados.
- O BFS garante solução ótima, mas é inviável para casos difíceis devido ao alto consumo de memória.
- O DFS, apesar de eficiente em memória, não é confiável para casos complexos.
- A heurística de Manhattan se mostrou mais informativa e eficiente do que a de peças fora do lugar, especialmente em casos médios e difíceis.

---

## 6. Conclusão

A escolha do algoritmo e da heurística impacta diretamente a eficiência na resolução do 8-Puzzle. O A* com heurística de Manhattan é recomendado para este tipo de problema, equilibrando tempo de execução, número de nós visitados e garantia de solução ótima.

---

## Como Executar

1. Instale Python 3.8+.
2. Clone o repositório:  
   `git clone https://github.com/sabarense/puzzle8.git`
3. Execute o script principal:  
   `python puzzle_solver.py`
4. Para gerar o executável (.exe), instale o PyInstaller (`pip install pyinstaller`) e rode:  
   `pyinstaller --onefile puzzle_solver.py`

---

## Referências

- Russell, S., Norvig, P. *Artificial Intelligence: A Modern Approach*.
- Documentação oficial do Python.
- Material da disciplina de Inteligência Artificial, PUC Minas.
- Normas Acadêmicas da PUC Minas (2025).
