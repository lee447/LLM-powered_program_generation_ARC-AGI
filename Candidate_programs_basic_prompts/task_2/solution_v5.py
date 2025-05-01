from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    # find the big monochrome rectangle color (excluding 0)
    from collections import Counter
    cnt = Counter(v for row in grid for v in row if v!=0)
    col_block = max(cnt, key=cnt.get)
    # find its bounding box
    r0, c0 = h, w
    r1 = c1 = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c]==col_block:
                r0, r1 = min(r0, r), max(r1, r)
                c0, c1 = min(c0, c), max(c1, c)
    bh, bw = r1-r0+1, c1-c0+1
    # extract the rectangle immediately above the block (or to the left if none)
    if r0>=bh:
        base_r, base_c = r0-bh, c0
    else:
        base_r, base_c = r0, c0-bw
    res = [[0]*bw for _ in range(bh)]
    for i in range(bh):
        for j in range(bw):
            r = base_r + i
            c = base_c + j
            if 0<=r<h and 0<=c<w and grid[r][c]!=col_block:
                res[i][j] = grid[r][c]
            else:
                res[i][j] = 0
    return res