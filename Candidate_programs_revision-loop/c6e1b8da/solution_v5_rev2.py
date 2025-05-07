from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[False]*W for _ in range(H)]
    shapes = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == col:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                rs = [r for r,c in cells]
                cs = [c for r,c in cells]
                r0,r1 = min(rs), max(rs)
                c0,c1 = min(cs), max(cs)
                shape = set((r-r0, c-c0) for r,c in cells)
                shapes.append({
                    'r0': r0, 'r1': r1,
                    'c0': c0, 'c1': c1,
                    'h': r1-r0+1, 'w': c1-c0+1,
                    'col': col, 'shape': shape
                })
    n = len(shapes)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if shapes[i]['r0'] <= shapes[j]['r1'] and shapes[j]['r0'] <= shapes[i]['r1']:
                adj[i].append(j)
                adj[j].append(i)
    visited_shape = [False]*n
    clusters = []
    for i in range(n):
        if not visited_shape[i]:
            stack = [i]
            visited_shape[i] = True
            cl = []
            while stack:
                u = stack.pop()
                cl.append(u)
                for v in adj[u]:
                    if not visited_shape[v]:
                        visited_shape[v] = True
                        stack.append(v)
            clusters.append(cl)
    out = [[0]*W for _ in range(H)]
    for cl in clusters:
        c0g = min(shapes[i]['c0'] for i in cl)
        offset = 0
        for k in sorted(cl, key=lambda x: shapes[x]['c0']):
            sh = shapes[k]
            start_c = c0g + offset
            for dr,dc in sh['shape']:
                out[sh['r0']+dr][start_c+dc] = sh['col']
            offset += sh['w']
    return out