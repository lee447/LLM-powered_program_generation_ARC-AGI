from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    full4 = [r for r in range(H) if all(grid[r][c] == 4 for c in range(W))]
    bounds = [-1] + full4 + [H]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(len(bounds)-1):
        top, bottom = bounds[i]+1, bounds[i+1]-1
        if top>bottom: continue
        visited = [[False]*W for _ in range(H)]
        seeds = []
        ones = []
        for r in range(top,bottom+1):
            for c in range(W):
                if visited[r][c]: continue
                v = grid[r][c]
                if v not in (0,1,4):
                    color = v
                elif v==1:
                    color = 1
                else:
                    continue
                stack = [(r,c)]
                comp = []
                visited[r][c] = True
                while stack:
                    pr,pc = stack.pop()
                    comp.append((pr,pc))
                    for dr,dc in dirs:
                        nr,nc = pr+dr, pc+dc
                        if top<=nr<=bottom and 0<=nc<W and not visited[nr][nc] and grid[nr][nc]==v:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                if color==1:
                    ones.append(comp)
                else:
                    seeds.append((color, comp))
        used_o = set()
        for color, sc in seeds:
            sset = set(sc)
            for j, oc in enumerate(ones):
                if j in used_o or len(oc)!=len(sc): continue
                oset = set(oc)
                found = False
                for ax,ay in sc:
                    for bx,by in oc:
                        dr = bx-ax; dc = by-ay
                        if all((x+dr,y+dc) in oset for x,y in sc):
                            for x,y in sc:
                                grid[x][y] = 1
                            for x,y in sc:
                                pass
                            for x,y in oc:
                                grid[x][y] = color
                            used_o.add(j)
                            found = True
                            break
                    if found: break
                if found: break
    return grid