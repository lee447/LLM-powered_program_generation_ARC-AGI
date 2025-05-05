from typing import List
import copy

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    bg = grid[0][0]
    res = copy.deepcopy(grid)
    blocks = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != bg:
                if v not in blocks:
                    blocks[v] = [r, r, c, c]
                else:
                    blocks[v][0] = min(blocks[v][0], r)
                    blocks[v][1] = max(blocks[v][1], r)
                    blocks[v][2] = min(blocks[v][2], c)
                    blocks[v][3] = max(blocks[v][3], c)
    items = sorted(blocks.items(), key=lambda x: x[1][0])
    for idx, (col, (r0, r1, c0, c1)) in enumerate(items):
        mask = [[grid[r][c] == col for c in range(c0, c1+1)] for r in range(r0, r1+1)]
        dx = -1 if idx % 2 == 0 else 1
        for r in range(r0, r1+1):
            for c in range(c0, c1+1):
                res[r][c] = bg
        for dr in range(r1 - r0 + 1):
            for dc in range(c1 - c0 + 1):
                if mask[dr][dc]:
                    nc = c0 + dc + dx
                    res[r0 + dr][nc] = col
    return res