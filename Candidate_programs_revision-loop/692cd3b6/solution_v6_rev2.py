from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    # find centers
    centers = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    # find the main block of 4s (largest connected component)
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    best_block = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 4 and not seen[r][c]:
                q = deque([(r,c)])
                comp = {(r,c)}
                seen[r][c] = True
                while q:
                    x,y = q.popleft()
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] == 4:
                            seen[nx][ny] = True
                            comp.add((nx,ny))
                            q.append((nx,ny))
                if len(comp) > len(best_block):
                    best_block = comp
    # for each square center, connect to main block if not already touching
    for (r0,c0) in centers:
        # if any neighbor is in block, skip
        if any((r0+dr,c0+dc) in best_block for dr,dc in dirs):
            continue
        # seeds are 4-connected neighbors of center that are zero or four
        seeds = [(r0+dr, c0+dc) for dr,dc in dirs
                 if 0<=r0+dr<h and 0<=c0+dc<w and grid[r0+dr][c0+dc] in (0,4)]
        if not seeds:
            continue
        # BFS from seeds to any block cell
        prev = {}
        q = deque()
        for s in seeds:
            q.append(s)
            prev[s] = None
        found = None
        while q and found is None:
            x,y = q.popleft()
            if (x,y) in best_block:
                found = (x,y)
                break
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if 0<=nx<h and 0<=ny<w and (nx,ny) not in prev and grid[nx][ny] in (0,4):
                    prev[(nx,ny)] = (x,y)
                    q.append((nx,ny))
        if found:
            # backtrack and fill zeros
            cur = found
            while cur is not None:
                x,y = cur
                if grid[x][y] == 0:
                    grid[x][y] = 4
                cur = prev[cur]
    return grid