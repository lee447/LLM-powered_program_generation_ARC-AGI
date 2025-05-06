def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import Counter, deque
    cnt = Counter(c for row in grid for c in row)
    X = min(cnt, key=lambda c: cnt[c])
    rows = [i for i in range(h) if any(grid[i][j]==X for j in range(w))]
    cols = [j for j in range(w) if any(grid[i][j]==X for i in range(h))]
    def spans(lst):
        spans,cur = [],[]
        for x in lst:
            if not cur or x==cur[-1]+1:
                cur.append(x)
            else:
                spans.append((cur[0],cur[-1]))
                cur=[x]
        if cur: spans.append((cur[0],cur[-1]))
        return spans
    rs, cs = spans(rows), spans(cols)
    m, n = len(rs), len(cs)
    if m>1:
        R = m+1
    else:
        R = rs[0][1]-rs[0][0]+1
    if n>1:
        C = n+1
    else:
        C = cs[0][1]-cs[0][0]+1
    out = [[0]*C for _ in range(R)]
    def pick_r(k):
        if m>1:
            if k==0: return rs[0][0]-1
            if k<m: return rs[k-1][1]+1
            return rs[-1][1]+1
        else:
            return rs[0][0]+k
    def pick_c(j):
        if n>1:
            if j==0: return cs[0][0]-1
            if j<n: return cs[j-1][1]+1
            return cs[-1][1]+1
        else:
            return cs[0][0]+j
    for i in range(R):
        for j in range(C):
            r, c = pick_r(i), pick_c(j)
            out[i][j] = grid[r][c]
    return out