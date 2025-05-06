import collections
def solve(grid):
    n,m=len(grid),len(grid[0])
    brow=[i for i in range(n) if all(grid[i][j]==4 for j in range(m))]
    bcol=[j for j in range(m) if all(grid[i][j]==4 for i in range(n))]
    rows=[i for i in range(n) if i not in brow]
    cols=[j for j in range(m) if j not in bcol]
    def intervals(a):
        iv=[]
        for x in a:
            if not iv or x!=iv[-1][-1]+1:
                iv.append([x])
            else:
                iv[-1].append(x)
        return iv
    rints, cints=intervals(rows),intervals(cols)
    cnt=collections.Counter(c for row in grid for c in row if c not in (0,1,4))
    if not cnt:
        return grid
    tc=cnt.most_common(1)[0][0]
    masks_by_shape={}
    for ri in rints:
        for ci in cints:
            h,w=len(ri),len(ci)
            mask=tuple(tuple(1 if grid[ri[i]][ci[j]]==tc else 0 for j in range(w)) for i in range(h))
            if any(any(r) for r in mask):
                masks_by_shape.setdefault((h,w),[]).append(mask)
    best_mask={shape:collections.Counter(lst).most_common(1)[0][0] for shape,lst in masks_by_shape.items()}
    ans=[row[:] for row in grid]
    for ri in rints:
        for ci in cints:
            h,w=len(ri),len(ci)
            shape=(h,w)
            if shape not in best_mask:
                continue
            mask=best_mask[shape]
            if any(grid[ri[i]][ci[j]]==tc for i in range(h) for j in range(w)):
                continue
            ok=True
            for i in range(h):
                for j in range(w):
                    if mask[i][j] and grid[ri[i]][ci[j]]!=1:
                        ok=False
                        break
                if not ok:
                    break
            if not ok:
                continue
            for i in range(h):
                for j in range(w):
                    if mask[i][j] and grid[ri[i]][ci[j]]==1:
                        ans[ri[i]][ci[j]]=tc
    return ans