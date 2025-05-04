from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bw = w // 3
    mapping = {
        'border': 3,
        'dot': 4,
        'diag': 9,
        'top': 6,
        'bot': 1
    }
    out = [[0]*w for _ in range(h)]
    for b in range(3):
        x = b*bw
        pos = {(r, c-x) for r in range(h) for c in range(x, x+bw) if grid[r][c]==5}
        if len(pos)==8:
            key = 'border'
        elif pos=={(1,1)}:
            key = 'dot'
        elif pos=={(0,2),(1,1),(2,0)}:
            key = 'diag'
        elif pos=={(0,0),(0,1),(0,2)}:
            key = 'top'
        elif pos=={(2,0),(2,1),(2,2)}:
            key = 'bot'
        else:
            key = None
        c = mapping[key]
        for r in range(h):
            for cc in range(x,x+bw):
                out[r][cc] = c
    return out