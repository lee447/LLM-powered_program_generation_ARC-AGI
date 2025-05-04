from typing import List
from collections import Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    barCols, barColors = [], []
    for c in range(W):
        cnt = Counter(grid[r][c] for r in range(H) if grid[r][c] != 0)
        if cnt:
            color, freq = cnt.most_common(1)[0]
            if freq > H // 2:
                barCols.append(c)
                barColors.append(color)
    pairs = sorted(zip(barCols, barColors))
    barCols = [c for c, _ in pairs]
    barColors = [col for _, col in pairs]
    barSet = set(barCols)
    bands = []
    for r in range(H):
        nonbar = [grid[r][c] for c in range(W) if c not in barSet]
        if nonbar:
            s = set(nonbar)
            if len(s) == 1 and nonbar[0] != 0:
                color = nonbar[0]
                full = all(grid[r][c] == color for c in range(W))
                bands.append((r, color, full))
    bands.sort(key=lambda x: x[0])
    B = len(barCols)
    def make_bg():
        row = [0]
        for bc in barColors:
            row += [bc, 0]
        return row
    def make_band(r, color, full):
        if full:
            return [color] * (2 * B + 1)
        row = [color]
        for c in barCols:
            row += [grid[r][c], color]
        return row
    out = [make_bg()]
    for r, color, full in bands:
        out.append(make_band(r, color, full))
        out.append(make_bg())
    return out