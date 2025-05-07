from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*W for _ in range(H)]
    shapes = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not seen[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                seen[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < H and 0 <= ny < W and not seen[nx][ny] and grid[nx][ny] == col:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                rs = [r for r,_ in cells]
                cs = [c0 for _,c0 in cells]
                r0, c0 = min(rs), min(cs)
                drs = [r-r0 for r,_ in cells]
                dcs = [c0-c0 for _,c0 in cells]  # placeholder to ensure list length
                shape = set((r-r0, c-c0) for r,c in cells)
                h = max(r-r0 for r,c in cells) + 1
                w = max(c-c0 for r,c in cells) + 1
                shapes.append({'r0': r0, 'c0': c0, 'r1': r0+h-1, 'h': h, 'w': w, 'col': col, 'shape': shape})
    n = len(shapes)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if shapes[i]['r0'] <= shapes[j]['r1'] and shapes[j]['r0'] <= shapes[i]['r1']:
                adj[i].append(j)
                adj[j].append(i)
    visited = [False]*n
    clusters = []
    for i in range(n):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            cl = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
                        cl.append(v)
            clusters.append(cl)
    out = [[0]*W for _ in range(H)]
    for cl in clusters:
        c0g = min(shapes[k]['c0'] for k in cl)
        offset = 0
        for k in sorted(cl, key=lambda k: shapes[k]['c0']):
            sh = shapes[k]
            nc = c0g + offset
            for dr,dc in sh['shape']:
                out[sh['r0']+dr][nc+dc] = sh['col']
            offset += sh['w']
    return out