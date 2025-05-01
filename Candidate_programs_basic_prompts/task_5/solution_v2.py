from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [[0] * (2 * W) for _ in range(2 * H)]
    for r in range(2 * H):
        for c in range(2 * W):
            if r < H and c < W:
                out[r][c] = grid[H - 1 - r][W - 1 - c]
            elif r < H and c >= W:
                out[r][c] = grid[H - 1 - r][c - W]
            elif r >= H and c < W:
                out[r][c] = grid[r - H][W - 1 - c]
            else:
                out[r][c] = grid[r - H][c - W]
    return out