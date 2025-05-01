from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    rows = [i for i in range(m) if any(grid[i][j] != 0 for j in range(n))]
    cols = [j for j in range(n) if any(grid[i][j] != 0 for i in range(m))]
    def clusters(a):
        res = []
        if not a: return res
        s = p = a[0]
        for x in a[1:]:
            if x == p + 1:
                p = x
            else:
                res.append((s, p))
                s = p = x
        res.append((s, p))
        return res
    row_clusters = clusters(rows)
    col_clusters = clusters(cols)
    minc, maxc = cols[0], cols[-1]
    gap_cols = set()
    for x, y in col_clusters:
        pass
    for (s1, e1), (s2, e2) in zip(col_clusters, col_clusters[1:]):
        for j in range(e1 + 1, s2):
            gap_cols.add(j)
    gap_rows_between = set()
    for (s1, e1), (s2, e2) in zip(row_clusters, row_clusters[1:]):
        for i in range(e1 + 1, s2):
            gap_rows_between.add(i)
    cluster_rows = set(i for s, e in row_clusters for i in range(s, e + 1))
    minr, maxr = rows[0], rows[-1]
    out = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            v = grid[i][j]
            if v != 0:
                out[i][j] = v
            else:
                if i in cluster_rows:
                    out[i][j] = 2 if j in gap_cols else 0
                elif i in gap_rows_between:
                    out[i][j] = 2 if minc <= j <= maxc else 1
                else:
                    out[i][j] = 1 if j in gap_cols else 0
    return out