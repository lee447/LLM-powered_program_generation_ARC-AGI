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
            segs = [grid[i][s:e] for s, e in segments]
            cnt = {}
            for seg in segs:
                for v in seg:
                    cnt[v] = cnt.get(v, 0) + 1
            items = sorted(cnt.items(), key=lambda x: -x[1])
            maj = items[0][0]
            minc = items[1][0] if len(items) > 1 else maj
            row = []
            for x in range(k):
                v = maj
                for seg in segs:
                    if seg[x] == minc:
                        v = minc
                        break
                row.append(v)
            res.append([border] + row + [border])
    return res