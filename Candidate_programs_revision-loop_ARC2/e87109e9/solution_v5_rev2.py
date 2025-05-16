from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    top_bg = grid[0][0]
    start = 0
    for i in range(h):
        if all(x != 0 for x in grid[i]) and any(x != top_bg for x in grid[i]):
            start = i
            break
    bottom = [row[:] for row in grid[start:]]
    H, W = len(bottom), len(bottom[0])
    cnt = {}
    for i in range(H):
        if all(bottom[i][j] == bottom[i][0] for j in range(W)):
            cnt[bottom[i][0]] = cnt.get(bottom[i][0], 0) + 1
    for j in range(W):
        if all(bottom[i][j] == bottom[0][j] for i in range(H)):
            cnt[bottom[0][j]] = cnt.get(bottom[0][j], 0) + 1
    line_color = max(cnt, key=cnt.get)
    rows = [i for i in range(H) if all(bottom[i][j] == line_color for j in range(W))]
    cols = [j for j in range(W) if all(bottom[i][j] == line_color for i in range(H))]
    def blocks(xs):
        res = []
        i = 0
        while i < len(xs):
            j = i
            while j+1 < len(xs) and xs[j+1] == xs[j] + 1:
                j += 1
            res.append((xs[i], xs[j]))
            i = j + 1
        return res
    rbs = blocks(rows)
    cbs = blocks(cols)
    row_blocks = []
    prev = -1
    for a,b in rbs:
        if prev+1 <= a-1:
            row_blocks.append((prev+1, a-1))
        prev = b
    if prev+1 <= H-1:
        row_blocks.append((prev+1, H-1))
    col_blocks = []
    prev = -1
    for a,b in cbs:
        if prev+1 <= a-1:
            col_blocks.append((prev+1, a-1))
        prev = b
    if prev+1 <= W-1:
        col_blocks.append((prev+1, W-1))
    cells = []
    for r0,r1 in row_blocks:
        for c0,c1 in col_blocks:
            cells.append((r0, r1, c0, c1))
    target = None
    for r0,r1,c0,c1 in cells:
        found = False
        for i in range(r0, r1+1):
            for j in range(c0, c1+1):
                if bottom[i][j] == 8:
                    found = True
                    break
            if found: break
        if found:
            target = (r1-r0+1, c1-c0+1)
            break
    new = [row[:] for row in bottom]
    if target:
        th, tw = target
        for r0,r1,c0,c1 in cells:
            if r1-r0+1 == th and c1-c0+1 == tw:
                for i in range(r0, r1+1):
                    for j in range(c0, c1+1):
                        new[i][j] = 8
    return new