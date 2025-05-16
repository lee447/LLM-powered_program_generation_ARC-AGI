from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    sep = 1
    # detect orientation
    horiz = any(all(cell == sep for cell in row) for row in grid)
    if horiz:
        # split by rows
        parts = []
        i = 0
        while i < h:
            if all(grid[i][j] == sep for j in range(w)):
                i += 1
            else:
                start = i
                while i < h and not all(grid[i][j] == sep for j in range(w)):
                    i += 1
                parts.append(grid[start:i])
        mask_block = parts[1]
        rect1 = parts[2]
        rect2 = parts[3]
        mh, mw = len(mask_block), len(mask_block[0])
        # select mask columns
        cols = [j for j in range(mw) if any(mask_block[i][j] != 0 for i in range(mh))]
        mask = [[mask_block[i][j] for j in cols] for i in range(mh)]
        r1c = next(c for row in rect1 for c in row if c != 0)
        r2c = next(c for row in rect2 for c in row if c != 0)
        out_h = len(rect1) + len(rect2) - 2
        out_w = len(cols)
        out = [[0]*out_w for _ in range(out_h)]
        for i in range(out_h):
            mi = i % mh
            for j in range(out_w):
                out[i][j] = r2c if mask[mi][j] != 0 else r1c
        return out
    else:
        # split by cols
        parts = []
        j = 0
        while j < w:
            if all(grid[i][j] == sep for i in range(h)):
                j += 1
            else:
                start = j
                while j < w and not all(grid[i][j] == sep for i in range(h)):
                    j += 1
                parts.append([row[start:j] for row in grid])
        mask_block = parts[1]
        rect1 = parts[2]
        rect2 = parts[3]
        mh, mw = len(mask_block), len(mask_block[0])
        rows = [i for i in range(mh) if any(mask_block[i][j] != 0 for j in range(mw))]
        mask = [[mask_block[i][j] for j in range(mw)] for i in rows]
        r1c = rect1[0][0]
        r2c = rect2[0][0]
        out_h = len(rows)
        out_w = len(rect1[0]) + len(rect2[0]) - 2
        out = [[0]*out_w for _ in range(out_h)]
        for i in range(out_h):
            for j in range(out_w):
                mj = j % mw
                out[i][j] = r2c if mask[i][mj] != 0 else r1c
        return out