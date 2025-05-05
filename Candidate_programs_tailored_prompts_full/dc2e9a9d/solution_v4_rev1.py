from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    rings = []
    for r in range(h - 4):
        for c in range(w - 4):
            if all(grid[r + dr][c + dc] == 3 for dr in (0, 4) for dc in range(5)) and \
               all(grid[r + dr][c + dc] == 3 for dc in (0, 4) for dr in range(5)) and \
               all(grid[r + dr][c + dc] == 0 for dr in range(1, 4) for dc in range(1, 4)):
                rings.append((r, c))
    red_squares = []
    for r in range(h - 4):
        for c in range(w - 4):
            if all(grid[r + dr][c + dc] == 1 for dr in range(5) for dc in range(5)):
                red_squares.append((r, c))
    if red_squares:
        r, c = red_squares[0]
        for dr in range(5):
            for dc in range(5):
                res[r + dr][c + dc] = 1 if (dr in (0, 4) or dc in (0, 4)) else 0
    else:
        if rings:
            idx = len(rings) // 2 if len(rings) >= 3 else 0
            r0, c0 = rings[idx]
            for dr in range(3):
                for dc in range(3):
                    if dr in (0, 2) or dc in (0, 2):
                        res[r0 + dr + 1][c0 + dc + 5] = 1
    if not red_squares and len(rings) >= 2:
        if len(rings) >= 3:
            r1, c1 = rings[1]
            r2, c2 = rings[2]
        else:
            r1, c1 = rings[0]
            r2, c2 = rings[1]
        top = r1 + 5 + ((r2 - (r1 + 5) - 3) // 2)
        left = c1 + 5 + ((c2 - (c1 + 5) - 3) // 2)
        for dr in range(3):
            for dc in range(3):
                if dr in (0, 2) or dc in (0, 2):
                    res[top + dr][left + dc] = 8
    return res