from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    m = len(grid)
    n = len(grid[0])
    rows = []
    cols = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                rows.append(i)
                cols.append(j)
    rows.sort()
    cols.sort()
    cr = rows[2]
    cc = cols[2]
    res = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                res[i][j] = 2
    for i in range(m):
        if grid[i][cc] != 2:
            if i < cr:
                d = cr-1 - i
            elif i > cr:
                d = i - (cr+1)
            else:
                continue
            res[i][cc] = 4 if d % 3 == 0 else 8
    for j in range(n):
        if grid[cr][j] != 2:
            if j < cc:
                d = cc-1 - j
            elif j > cc:
                d = j - (cc+1)
            else:
                continue
            res[cr][j] = 4 if d % 3 == 0 else 8
    for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        i = cr + dr
        j = cc + dc
        while 0 <= i < m and 0 <= j < n:
            if grid[i][j] != 2:
                res[i][j] = 1
            i += dr
            j += dc
    return res