from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    best_area = 0
    best_matches = []
    best_h = best_w = 0
    for h in range(H, 1, -1):
        if h * W < best_area:
            break
        for w in range(W, 1, -1):
            area = h * w
            if area < best_area:
                break
            subs = {}
            for i in range(0, H - h + 1):
                for j in range(0, W - w + 1):
                    key = tuple(tuple(grid[i + di][j + dj] for dj in range(w)) for di in range(h))
                    if any(cell != 0 for row in key for cell in row):
                        subs.setdefault(key, []).append((i, j))
            for key, poses in subs.items():
                if len(poses) >= 2:
                    if area > best_area:
                        best_area = area
                        best_matches = poses[:]
                        best_h, best_w = h, w
                    elif area == best_area:
                        best_matches.extend(poses)
        # continue to next h
    out = [[0] * W for _ in range(H)]
    for i, j in best_matches:
        for di in range(best_h):
            for dj in range(best_w):
                out[i + di][j + dj] = grid[i + di][j + dj]
    return out