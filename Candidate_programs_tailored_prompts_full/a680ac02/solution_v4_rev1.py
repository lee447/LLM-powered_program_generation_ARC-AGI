from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    frames = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and grid[nr][nc] == col:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,_ in comp]; cs = [c for _,c in comp]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                if r1-r0+1 == 4 and c1-c0+1 == 4 and len(comp) == 16:
                    hollow = True
                    for rr in range(r0+1, r1):
                        for cc in range(c0+1, c1):
                            if grid[rr][cc] != 0:
                                hollow = False
                                break
                        if not hollow:
                            break
                    if hollow:
                        frames.append((r0, c0))
    m = len(frames)
    def overlap(a0,a1,b0,b1):
        return not (a1 < b0 or b1 < a0)
    def is_connected(frames, dim):
        n = len(frames)
        if n <= 1:
            return True
        spans = []
        for r0,c0 in frames:
            if dim == 'row':
                spans.append((r0, r0+3))
            else:
                spans.append((c0, c0+3))
        adj = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i+1, n):
                if overlap(spans[i][0], spans[i][1], spans[j][0], spans[j][1]):
                    adj[i].append(j)
                    adj[j].append(i)
        seen = {0}
        stack = [0]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        return len(seen) == n
    if is_connected(frames, 'row'):
        orient = 'H'
    elif is_connected(frames, 'col'):
        orient = 'V'
    else:
        orient = 'H'
    if orient == 'H':
        frames.sort(key=lambda x: x[1])
        out = [[0]*(4*m) for _ in range(4)]
        for idx, (r0, c0) in enumerate(frames):
            for dr in range(4):
                for dc in range(4):
                    out[dr][idx*4 + dc] = grid[r0+dr][c0+dc]
    else:
        frames.sort(key=lambda x: x[0])
        out = [[0]*4 for _ in range(4*m)]
        for idx, (r0, c0) in enumerate(frames):
            for dr in range(4):
                for dc in range(4):
                    out[idx*4 + dr][dc] = grid[r0+dr][c0+dc]
    return out