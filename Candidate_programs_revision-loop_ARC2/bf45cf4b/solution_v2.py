def solve(grid):
    h=len(grid); w=len(grid[0])
    from collections import Counter
    cnt=Counter(c for row in grid for c in row)
    bg,_=cnt.most_common()[-1] if len(cnt)>1 else cnt.most_common()[0]
    def rot90(b):
        return list(zip(*b[::-1]))
    best_k=0; best=None
    for k in range(min(h,w),1,-1):
        for i in range(h-k+1):
            for j in range(w-k+1):
                b=[row[j:j+k] for row in grid[i:i+k]]
                if all(b[x][y]==b[k-1-y][x] for x in range(k) for y in range(k)):
                    if k>best_k:
                        best_k=k; best=[row[:] for row in b]
        if best_k: break
    k=best_k; pat=best
    H=(h//k-(1 if h%k<k else 0))*k or h
    W=(w//k-(1 if w%k<k else 0))*k or w
    out=[[bg]*W for _ in range(H)]
    for bi in range(H//k):
        for bj in range(W//k):
            if (bi+ bj)%2==0:
                for x in range(k):
                    for y in range(k):
                        out[bi*k+x][bj*k+y]=pat[x][y]
    return out