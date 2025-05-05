from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    C = w // 2
    bg = grid[0][0]
    stripes = [r for r in range(h) if all(grid[r][c] == bg for c in range(C))]
    out = [[bg]*C for _ in range(h)]
    bands = [(stripes[i]+1, stripes[i+1]) for i in range(len(stripes)-1)]
    colors = []
    for top, bot in bands:
        s = {grid[r][c] for r in range(top, bot) for c in range(C, w) if grid[r][c] not in (bg,0)}
        colors.append(next(iter(s)))
    if colors:
        m = len(colors)
        mapping = {colors[i]: colors[(i+1)%m] for i in range(m)}
    for (top, bot), col in zip(bands, colors):
        color = mapping[col]
        band = bot - top
        for i, r in enumerate(range(top, bot)):
            cnt = sum(grid[r][c] not in (bg,0) for c in range(C, w))
            if band > 1:
                mx = max(sum(grid[x][c] not in (bg,0) for c in range(C, w)) for x in range(top, bot))
                mn = min(sum(grid[x][c] not in (bg,0) for c in range(C, w)) or mx for x in range(top, bot))
                if cnt == mn:
                    wi = mx - (mn - mn)
                else:
                    wi = mx - (cnt - mn)
            else:
                wi = cnt
            off = (C - wi) // 2
            for c in range(off, off + wi):
                out[r][c] = color
    return out