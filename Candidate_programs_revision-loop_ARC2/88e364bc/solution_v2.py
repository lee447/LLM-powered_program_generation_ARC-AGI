from typing import List
import math

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    new_grid = [row[:] for row in grid]
    dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    visited_marker = set()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 4 and (i,j) not in visited_marker:
                # find v by checking 8 neighbors
                v = None
                for di,dj in dirs:
                    ni,nj = i+di, j+dj
                    if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] not in (0,4):
                        v = grid[ni][nj]
                        break
                if v is None:
                    continue
                # BFS comp of v or 4
                comp = []
                seen = set()
                stack = [(i,j)]
                while stack:
                    ci,cj = stack.pop()
                    if (ci,cj) in seen: continue
                    if grid[ci][cj] not in (v,4): continue
                    seen.add((ci,cj))
                    comp.append((ci,cj))
                    for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                        ni,nj = ci+di, cj+dj
                        if 0 <= ni < h and 0 <= nj < w:
                            stack.append((ni,nj))
                # sort comp in clockwise order around centroid
                cy = sum(x for x,y in comp) / len(comp)
                cx = sum(y for x,y in comp) / len(comp)
                comp_sorted = sorted(comp, key=lambda p: -math.atan2(p[0]-cy, p[1]-cx))
                # find index of marker
                idx = comp_sorted.index((i,j))
                new_pos = comp_sorted[(idx+1) % len(comp_sorted)]
                # move marker
                new_grid[i][j] = v
                ni,nj = new_pos
                new_grid[ni][nj] = 4
                visited_marker.add((ni,nj))
    return new_grid