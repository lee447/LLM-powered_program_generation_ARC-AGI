from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    mask0 = [[grid[i][j] != 0 for j in range(m)] for i in range(n)]
    mask = [row[:] for row in mask0]
    for _ in range(2):
        new = [[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mask[i][j]:
                    for di in (-1,0,1):
                        for dj in (-1,0,1):
                            ni, nj = i+di, j+dj
                            if 0 <= ni < n and 0 <= nj < m:
                                new[ni][nj] = True
        mask = new
    labels = [[-1]*m for _ in range(n)]
    cid = 0
    for i in range(n):
        for j in range(m):
            if mask[i][j] and labels[i][j] < 0:
                dq = deque([(i,j)])
                labels[i][j] = cid
                while dq:
                    x,y = dq.popleft()
                    for dx in (-1,0,1):
                        for dy in (-1,0,1):
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < n and 0 <= ny < m and mask[nx][ny] and labels[nx][ny] < 0:
                                labels[nx][ny] = cid
                                dq.append((nx,ny))
                cid += 1
    count = [0]*cid
    for i in range(n):
        for j in range(m):
            if mask0[i][j]:
                lbl = labels[i][j]
                if lbl >= 0:
                    count[lbl] += 1
    best = max(range(cid), key=lambda k: count[k]) if cid>0 else -1
    minr, maxr, minc, maxc = n, -1, m, -1
    for i in range(n):
        for j in range(m):
            if mask0[i][j] and labels[i][j] == best:
                if i < minr: minr = i
                if i > maxr: maxr = i
                if j < minc: minc = j
                if j > maxc: maxc = j
    if minr > maxr or minc > maxc:
        return []
    h, w = maxr-minr+1, maxc-minc+1
    s = max(h, w)
    if w < s:
        diff = s-w
        maxc = min(m-1, maxc+diff)
    if h < s:
        diff = s-h
        maxr = min(n-1, maxr+diff)
    return [row[minc:maxc+1] for row in grid[minr:maxr+1]]