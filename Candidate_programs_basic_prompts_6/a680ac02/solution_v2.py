from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    shapes = []
    for r in range(h-3):
        for c in range(w-3):
            cval = grid[r][c]
            if cval == 0: continue
            ok = True
            for i in range(4):
                for j in range(4):
                    if i in (0,3) or j in (0,3):
                        if grid[r+i][c+j] != cval: ok = False
                    else:
                        if grid[r+i][c+j] != 0: ok = False
            if ok:
                shapes.append((r, c, cval))
    blocks = {}
    for r, c, v in shapes:
        blocks[(r,c)] = [grid[r+i][c:c+4] for i in range(4)]
    if not shapes:
        return []
    horizontal = True
    for i in range(len(shapes)):
        for j in range(i+1, len(shapes)):
            ci, cj = shapes[i][1], shapes[j][1]
            if ci <= cj+3 and cj <= ci+3:
                horizontal = False
    if horizontal:
        shapes.sort(key=lambda x: x[1])
        out = [[ ] for _ in range(4)]
        for r, c, v in shapes:
            blk = blocks[(r,c)]
            for i in range(4):
                out[i].extend(blk[i])
        return out
    else:
        shapes.sort(key=lambda x: x[0])
        out = []
        for r, c, v in shapes:
            out.extend(blocks[(r,c)])
        return out