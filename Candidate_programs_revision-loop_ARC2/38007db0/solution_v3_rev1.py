from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    nR, nC = len(grid), len(grid[0])
    border = grid[0][0]
    col_sep = set(j for j in range(nC) if all(grid[i][j] == border for i in range(nR)))
    segments = []
    j = 0
    while j < nC:
        if j in col_sep:
            j += 1
        else:
            start = j
            while j < nC and j not in col_sep:
                j += 1
            segments.append((start, j))
    k = segments[0][1] - segments[0][0]
    res = []
    for i in range(nR):
        if all(grid[i][j] == border for j in range(nC)):
            res.append([border] * (k + 2))
        else:
            row = []
            for x in range(k):
                vals = [grid[i][s + x] for s, e in segments]
                cnt = {}
                for v in vals:
                    cnt[v] = cnt.get(v, 0) + 1
                minf = min(cnt.values())
                choices = [v for v, f in cnt.items() if f == minf]
                row.append(min(choices))
            res.append([border] + row + [border])
    return res