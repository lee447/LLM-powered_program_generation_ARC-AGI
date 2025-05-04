from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0])
    out = [[0]*W for _ in range(H)]
    for j in range(W):
        entries = [(i, grid[i][j]) for i in range(H) if grid[i][j] != 0]
        anchors = [(i, c) for i, c in entries if c == 5]
        if anchors:
            non_anchors = sorted((i, c) for i, c in entries if c != 5)
            prev = -1
            for i, c in non_anchors:
                for r in range(prev+1, i+1):
                    out[r][j] = c
                prev = i
            for r in range(prev+1, H):
                out[r][j] = 5
        else:
            for i, c in entries:
                out[i][j] = c
    return out