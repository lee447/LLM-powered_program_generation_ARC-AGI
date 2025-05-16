def solve(grid):
    h=len(grid); w=len(grid[0])
    from collections import defaultdict
    freq=defaultdict(int)
    for r in range(h):
        for c in range(w):
            freq[grid[r][c]]+=1
    bg=max(freq, key=lambda x:freq[x])
    colors=[c for c in freq if c!=bg]
    seeds={c:[] for c in colors}
    for r in range(h):
        for c in range(w):
            v=grid[r][c]
            if v in seeds: seeds[v].append((r,c))
    def pickA():
        for c in colors:
            if len(seeds[c])==2: return c
        for c in colors:
            cr=defaultdict(int); sr=defaultdict(int)
            for r,c0 in seeds[c]:
                cr[r+c0]+=1; sr[c0-r]+=1
            if any(cr[k]>1 for k in cr) or any(sr[k]>1 for k in sr): return c
        return colors[0]
    A=pickA()
    B=[c for c in colors if c!=A]
    B=B[0] if B else None
    sA=seeds[A]
    oriA=None; dA=None
    if len(sA)==2 and sA[0][0]+sA[0][1]==sA[1][0]+sA[1][1]:
        oriA='anti'; dA=sA[0][0]+sA[0][1]
    else:
        oriA='diag'; dA=sA[0][1]-sA[0][0]
        if len(sA)>1:
            for i in range(1,len(sA)):
                if sA[i][1]-sA[i][0]==dA: break
    out=[row[:] for row in grid]
    if oriA=='anti':
        rs=sorted([r for r,_ in sA]); r0,r1=rs[0],rs[-1]
        for r in range(r0,r1+1):
            c=dA-r
            if 0<=c<w and out[r][c]==bg: out[r][c]=A
    else:
        rs=sorted([r for r,_ in sA]); r0,r1=rs[0],rs[-1]
        for r in range(r0,r1+1):
            c=r+dA
            if 0<=c<w and out[r][c]==bg: out[r][c]=A
    if B is not None:
        oriB='anti' if oriA=='diag' else 'diag'
        onA=[]
        for r,c in seeds[B]:
            if oriA=='anti' and r+c==dA: onA.append((r,c))
            if oriA=='diag' and c-r==dA: onA.append((r,c))
        ks=set()
        for r,c in onA:
            ks.add((r+c) if oriB=='anti' else (c-r))
        for k in ks:
            if oriB=='anti':
                r0=max(0,k-(w-1)); r1=min(h-1,k)
                for r in range(r0,r1+1):
                    c=k-r
                    if 0<=c<w and out[r][c]==bg: out[r][c]=B
            else:
                r0=max(0,-k); r1=min(h-1,w-1-k)
                for r in range(r0,r1+1):
                    c=r+k
                    if 0<=c<w and out[r][c]==bg: out[r][c]=B
    return out