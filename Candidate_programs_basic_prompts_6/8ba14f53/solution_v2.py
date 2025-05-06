from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bw = w // 3
    blocks = []
    for bi in range(3):
        block = [row[bi*bw:(bi+1)*bw] for row in grid]
        blocks.append(block)
    shrunk = []
    for b in blocks:
        nz_rows = [i for i, row in enumerate(b) if any(c != 0 for c in row)]
        if len(nz_rows) >= 3:
            sel = nz_rows[:3]
        else:
            sel = nz_rows + [i for i in range(4) if i not in nz_rows][:3-len(nz_rows)]
        shrunk.append([b[i] for i in sel])
    res = [[0]*bw for _ in range(bw)]
    for sb in shrunk:
        for i in range(bw):
            for j in range(bw):
                if sb[i][j] != 0:
                    res[i][j] = sb[i][j]
    return res