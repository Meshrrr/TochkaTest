
import sys

from collections import deque

# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]

def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]


def solve(grid):
    starts = []
    keys = {}
    total_keys = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            cell = grid[i][j]
            if cell == '@':
                starts.append((i, j))
            elif 'a' <= cell <= 'z':
                keys[cell] = (i, j)
                total_keys += 1


    if len(starts) != 4:
        return -1


    initial_state = (*starts[0], *starts[1], *starts[2], *starts[3], frozenset())

    queue = deque([(0, initial_state)])
    visited = set([initial_state])

    directions = [(-1, 0), (1,0), (0, -1), (0, 1)]

    while queue:
        steps, state = queue.popleft()
        r1, c1, r2, c2, r3, c3, r4, c4, collected = state

        if len(collected) == total_keys:
            return steps

        for robot in range(4):
            r, c = [r1, r2, r3, r4][robot], [c1, c2, c3, c4][robot]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                    continue
                if grid[nr][nc] == '#':
                    continue

                cell = grid[nr][nc]
                if 'A' <= cell <= 'Z' and cell.lower() not in collected:
                    continue

                new_collected = set(collected)
                if 'a' <= cell <= 'z':
                    new_collected.add(cell)

                new_positions = [r1, c1, r2, c2, r3, c3, r4, c4]
                new_positions[robot*2] = nr
                new_positions[robot*2+1] = nc
                new_state = (*new_positions, frozenset(new_collected))

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((steps + 1, new_state))

    return -1

def main():
    data = get_input()
    result = solve(data)
    print(result)


if __name__ == '__main__':
    main()