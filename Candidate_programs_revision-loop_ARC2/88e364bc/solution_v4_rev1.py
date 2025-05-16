from typing import List
import math

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    new_grid = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 4:
                v = None
                for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] not in (0,4):
                        v = grid[ni][nj]
                        break
                if v is None:
                    continue
                seed = None
                for di, dj in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == v:
                        seed = (ni, nj)
                        break
                if seed is None:
                    continue
                seen = set()
                stack = [seed]
                comp = []
                while stack:
                    x, y = stack.pop()
                    if (x,y) in seen or grid[x][y] != v:
                        continue
                    seen.add((x,y))
                    comp.append((x,y))
                    for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x+di, y+dj
                        if 0 <= nx < h and 0 <= ny < w:
                            stack.append((nx,ny))
                cy = sum(x for x,y in comp) / len(comp)
                cx = sum(y for x,y in comp) / len(comp)
                comp_sorted = sorted(comp, key=lambda p: math.atan2(p[0]-cy, p[1]-cx))
                ring_nei = [(i+di, j+dj) for di,dj in [(-1,0),(1,0),(0,-1),(0,1)] if 0<=i+di<h and 0<=j+dj<w and grid[i+di][j+dj]==v]
                if not ring_nei:
                    continue
                r0 = ring_nei[0]
                idx = comp_sorted.index(r0)
                r1 = comp_sorted[(idx-1) % len(comp_sorted)]
                best_dot = None
                ni = nj = None
                vx = cx - r1[1]
                vy = cy - r1[0]
                for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                    x2, y2 = r1[0]+di, r1[1]+dj
                    if 0 <= x2 < h and 0 <= y2 < w and grid[x2][y2] != v:
                        dot = (y2 - r1[1]) * vx + (x2 - r1[0]) * vy
                        if best_dot is None or dot > best_dot:
                            best_dot = dot
                            ni, nj = x2, y2
                if ni is None:
                    continue
                new_grid[i][j] = grid[ni][nj]
                new_grid[ni][nj] = 4
    return new_grid