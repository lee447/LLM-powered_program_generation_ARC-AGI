from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                val = grid[i][j]
                stack = [(i, j)]
                cells = []
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    cells.append((r, c))
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] != 0 and not visited[rr][cc]:
                            visited[rr][cc] = True
                            stack.append((rr, cc))
                comps.append({'cells': cells, 'val': val})
    def mirror_pair(a, b):
        if len(a['cells']) != len(b['cells']): return False
        rows_a = {}
        rows_b = {}
        for r, c in a['cells']:
            rows_a.setdefault(r, []).append(c)
        for r, c in b['cells']:
            rows_b.setdefault(r, []).append(c)
        if set(rows_a) != set(rows_b): return False
        for r in rows_a:
            ca = sorted(rows_a[r])
            cb = sorted(rows_b[r])
            m = len(ca)
            for k in range(m):
                if (ca[k] + cb[m-1-k]) / 2 != (ca[0] + cb[-1]) / 2:
                    return False
        return True
    n = len(comps)
    pair = {}
    for i in range(n):
        for j in range(i+1, n):
            if mirror_pair(comps[i], comps[j]):
                pair[i] = j
                pair[j] = i
    newval = [comps[i]['val'] for i in range(n)]
    for i, j in pair.items():
        if i < j:
            newval[i] = 2
            newval[j] = 2
    out = [[0]*w for _ in range(h)]
    for idx, comp in enumerate(comps):
        for r, c in comp['cells']:
            out[r][c] = newval[idx]
    return out