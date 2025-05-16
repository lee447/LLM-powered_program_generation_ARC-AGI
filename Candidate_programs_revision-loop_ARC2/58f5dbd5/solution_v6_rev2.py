from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    rb = [i for i in range(h) if all(grid[i][j] == border for j in range(w))]
    cs = [j for j in range(w) if all(grid[i][j] == border for i in range(h))]
    rsegs = [(rb[i]+1, rb[i+1]-1) for i in range(len(rb)-1) if rb[i+1]-rb[i]>1]
    csegs = [(cs[i]+1, cs[i+1]-1) for i in range(len(cs)-1) if cs[i+1]-cs[i]>1]
    orient = 'col' if len(csegs) < len(rsegs) else 'row'
    prim = csegs if orient=='col' else rsegs
    oth = rsegs if orient=='col' else csegs
    best_i, best_score = 0, -1
    for i,(a,b) in enumerate(prim):
        cnt = 0
        for (c,d) in oth:
            found = False
            if orient=='col':
                for y in range(c,d+1):
                    for x in range(a,b+1):
                        if grid[y][x] != border:
                            found = True
                            break
                    if found: break
            else:
                for y in range(a,b+1):
                    for x in range(c,d+1):
                        if grid[y][x] != border:
                            found = True
                            break
                    if found: break
            if found: cnt += 1
        score = cnt * (b-a+1)
        if score > best_score:
            best_score, best_i = score, i
    a,b = prim[best_i]
    out = []
    if orient=='row':
        out.append([border]*w)
        for i in range(a,b+1):
            out.append(grid[i][:])
        out.append([border]*w)
    else:
        for row in grid:
            out.append([border] + row[a:b+1] + [border])
    return out