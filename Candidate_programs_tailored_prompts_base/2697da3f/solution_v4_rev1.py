from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 4]
    min_r = min(r for r, _ in pts)
    max_r = max(r for r, _ in pts)
    min_c = min(c for _, c in pts)
    max_c = max(c for _, c in pts)
    tile = [row[min_c:max_c+1] for row in grid[min_r:max_r+1]]
    th, tw = len(tile), len(tile[0])
    pivot_i = (th - 1) // 2
    pivot_j = (tw - 1) // 2
    d = tw
    if d % 2 == 1:
        N = 3 * d
    else:
        N = 3 * d - 1
    res = [[0]*N for _ in range(N)]
    center = N // 2
    for i in range(th):
        for j in range(tw):
            if tile[i][j] != 4:
                continue
            dr = i - pivot_i
            dc = j - pivot_j
            # West
            r = center + dr
            c = center + dc - d
            if 0 <= r < N and 0 <= c < N:
                res[r][c] = 4
            # North
            r = center - dc - d
            c = center + dr
            if 0 <= r < N and 0 <= c < N:
                res[r][c] = 4
            # East
            r = center + dr
            c = center + dc + d
            if 0 <= r < N and 0 <= c < N:
                res[r][c] = 4
            # South
            r = center + dc + d
            c = center + dr
            if 0 <= r < N and 0 <= c < N:
                res[r][c] = 4
    return res