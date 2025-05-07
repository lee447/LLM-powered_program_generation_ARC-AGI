from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    bs = (n - 4) // 3
    step = bs + 1
    out = [[0] * n for _ in range(n)]
    for bi in range(3):
        for bj in range(3):
            top = 1 + bi * step
            left = 1 + bj * step
            vals = {}
            for i in range(bs):
                for j in range(bs):
                    v = grid[top + i][left + j]
                    if v != 0:
                        vals[v] = vals.get(v, 0) + 1
            c1, c2 = list(vals.keys())
            cnt1, cnt2 = vals[c1], vals[c2]
            if cnt1 == 9:
                shape_in, bg_in, typ = c1, c2, 'plus'
            elif cnt2 == 9:
                shape_in, bg_in, typ = c2, c1, 'plus'
            elif cnt1 == 3:
                shape_in, bg_in, typ = c1, c2, 'L'
            else:
                shape_in, bg_in, typ = c2, c1, 'L'
            shape_out, bg_out = bg_in, shape_in
            for i in range(bs):
                for j in range(bs):
                    out[top + i][left + j] = bg_out
            if typ == 'plus':
                m = bs // 2
                for k in range(bs):
                    out[top + m][left + k] = shape_out
                    out[top + k][left + m] = shape_out
            else:
                coords = [(i, j) for i in range(bs) for j in range(bs) if grid[top + i][left + j] == shape_in]
                if max(i for i, j in coords) <= 1 and max(j for i, j in coords) <= 1:
                    pts = [(0, 0), (0, 1), (1, 0)]
                elif max(i for i, j in coords) <= 1 and min(j for i, j in coords) >= bs - 2:
                    pts = [(0, bs - 1), (0, bs - 2), (1, bs - 1)]
                elif min(i for i, j in coords) >= bs - 2 and max(j for i, j in coords) <= 1:
                    pts = [(bs - 1, 0), (bs - 1, 1), (bs - 2, 0)]
                else:
                    pts = [(bs - 1, bs - 1), (bs - 1, bs - 2), (bs - 2, bs - 1)]
                for dx, dy in pts:
                    out[top + dx][left + dy] = shape_out
    return out