def solve(grid):
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    blocks = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not visited[i][j]:
                color = grid[i][j]
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<H and 0<=nc<W and not visited[nr][nc] and grid[nr][nc]==color:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,_ in comp]; cs = [c for _,c in comp]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                frame = []
                for r in range(r0, r1+1):
                    for c in (c0, c1):
                        frame.append((r,c))
                for c in range(c0+1, c1):
                    for r in (r0, r1):
                        frame.append((r,c))
                blocks.append({'r0':r0,'r1':r1,'c0':c0,'c1':c1,'color':color,'frame':frame})
    n = len(blocks)
    def overlap(a,b,dim):
        if dim=='row':
            return not (a['r1']<b['r0'] or b['r1']<a['r0'])
        else:
            return not (a['c1']<b['c0'] or b['c1']<a['c0'])
    def find_comp(dim):
        adj = {i:[] for i in range(n)}
        for i in range(n):
            for j in range(i+1,n):
                if overlap(blocks[i],blocks[j],dim):
                    adj[i].append(j); adj[j].append(i)
        seen=set()
        for i in range(n):
            if i not in seen:
                stack=[i]; comp=[]
                seen.add(i)
                while stack:
                    u=stack.pop(); comp.append(u)
                    for v in adj[u]:
                        if v not in seen:
                            seen.add(v); stack.append(v)
                if len(comp)==n//2:
                    return comp
        return None
    horiz = find_comp('row')
    if horiz is not None:
        chosen = sorted(horiz, key=lambda i: blocks[i]['c0'])
        outH, outW = 4, 4*(n//2)
        out = [[0]*outW for _ in range(outH)]
        for idx,i in enumerate(chosen):
            b = blocks[i]
            dr = -b['r0']; dc = -b['c0'] + idx*4
            for r,c in b['frame']:
                out[r+dr][c+dc] = b['color']
    else:
        vert = find_comp('col')
        chosen = sorted(vert, key=lambda i: blocks[i]['r0'])
        outH, outW = 4*(n//2), 4
        out = [[0]*outW for _ in range(outH)]
        for idx,i in enumerate(chosen):
            b = blocks[i]
            dr = -b['r0'] + idx*4; dc = -b['c0']
            for r,c in b['frame']:
                out[r+dr][c+dc] = b['color']
    return out