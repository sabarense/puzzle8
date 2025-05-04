import heapq
from collections import deque
import time

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)


class Node:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    def __lt__(self, other):
        return False


def get_neighbors(state):
    idx = state.index(0)
    row, col = divmod(idx, 3)
    moves = []
    if row > 0: moves.append(-3)  # up
    if row < 2: moves.append(3)  # down
    if col > 0: moves.append(-1)  # left
    if col < 2: moves.append(1)  # right

    neighbors = []
    for move in moves:
        new_idx = idx + move
        new_state = list(state)
        new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
        neighbors.append(tuple(new_state))
    return neighbors


def reconstruct_path(node):
    path = []
    while node.parent:
        path.append(node.state)
        node = node.parent
    path.append(node.state)
    return path[::-1]


def misplaced_tiles(state, goal=GOAL_STATE):
    return sum(1 for i in range(9) if state[i] != goal[i] and state[i] != 0)


def manhattan_distance(state, goal=GOAL_STATE):
    distance = 0
    for num in range(1, 9):
        x1, y1 = divmod(state.index(num), 3)
        x2, y2 = divmod(goal.index(num), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


def bfs(start_state):
    start_time = time.time()
    visited = set()
    queue = deque([Node(start_state)])
    nodes_expanded = 0

    while queue:
        node = queue.popleft()
        nodes_expanded += 1

        if node.state == GOAL_STATE:
            return reconstruct_path(node), nodes_expanded, time.time() - start_time

        visited.add(node.state)
        for neighbor in get_neighbors(node.state):
            if neighbor not in visited:
                queue.append(Node(neighbor, node, None, node.depth + 1))

    return None, nodes_expanded, time.time() - start_time


def dfs(start_state, max_depth=50):
    start_time = time.time()
    visited = set()
    stack = [Node(start_state)]
    nodes_expanded = 0

    while stack:
        node = stack.pop()
        nodes_expanded += 1

        if node.state == GOAL_STATE:
            return reconstruct_path(node), nodes_expanded, time.time() - start_time

        if node.depth < max_depth:
            visited.add(node.state)
            for neighbor in get_neighbors(node.state):
                if neighbor not in visited:
                    stack.append(Node(neighbor, node, None, node.depth + 1))

    return None, nodes_expanded, time.time() - start_time


def a_star(start_state, heuristic):
    start_time = time.time()
    visited = set()
    heap = []
    start_node = Node(start_state)
    heapq.heappush(heap, (heuristic(start_state), 0, start_node))
    nodes_expanded = 0

    while heap:
        f, g, node = heapq.heappop(heap)
        nodes_expanded += 1

        if node.state == GOAL_STATE:
            return reconstruct_path(node), nodes_expanded, time.time() - start_time

        visited.add(node.state)
        for neighbor in get_neighbors(node.state):
            if neighbor not in visited:
                h = heuristic(neighbor)
                heapq.heappush(heap, (g + 1 + h, g + 1, Node(neighbor, node, None, node.depth + 1)))

    return None, nodes_expanded, time.time() - start_time


def print_board(state):
    print("+---+---+---+")
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print("| {} | {} | {} |".format(*[x if x != 0 else ' ' for x in row]))
        print("+---+---+---+")


def print_header(title):
    print("\n" + "=" * 50)
    print(f" {title.upper()} ")
    print("=" * 50)


def run_tests(cases):
    for case_name, initial_state in cases.items():
        print_header(f"Teste: {case_name}")
        print(" Estado Inicial:")
        print_board(initial_state)

        # BFS
        path, nodes, t = bfs(initial_state)
        print("\n[ BFS ]")
        if path:
            print(f" → Movimentos: {len(path) - 1}")
            print(f" → Nós expandidos: {nodes}")
            print(f" → Tempo: {t:.4f}s")
        else:
            print(" × Solução não encontrada")

        # DFS
        path, nodes, t = dfs(initial_state)
        print("\n[ DFS ]")
        if path:
            print(f" → Movimentos: {len(path) - 1}")
            print(f" → Nós expandidos: {nodes}")
            print(f" → Tempo: {t:.4f}s")
        else:
            print(" × Solução não encontrada")

        # A* Manhattan
        path, nodes, t = a_star(initial_state, manhattan_distance)
        print("\n[ A* (Manhattan) ]")
        if path:
            print(f" → Movimentos: {len(path) - 1}")
            print(f" → Nós expandidos: {nodes}")
            print(f" → Tempo: {t:.4f}s")
        else:
            print(" × Solução não encontrada")

        # A* Misplaced
        path, nodes, t = a_star(initial_state, misplaced_tiles)
        print("\n[ A* (Peças Fora) ]")
        if path:
            print(f" → Movimentos: {len(path) - 1}")
            print(f" → Nós expandidos: {nodes}")
            print(f" → Tempo: {t:.4f}s")
        else:
            print(" × Solução não encontrada")

        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    test_cases = {
        "Caso Fácil": (1, 2, 3, 4, 5, 6, 7, 0, 8),
        "Caso Médio": (2, 8, 1, 0, 4, 3, 7, 6, 5),
        "Caso Difícil": (8, 6, 7, 2, 5, 4, 3, 0, 1)
    }

    print_header("8-Puzzle Solver")
    run_tests(test_cases)
    input("Pressione ENTER para sair...")

