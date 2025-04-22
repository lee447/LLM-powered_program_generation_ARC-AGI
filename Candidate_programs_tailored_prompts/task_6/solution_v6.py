def solve(grid):
    n = len(grid)
    m = len(grid[0])
    non = [(i,j) for i in range(n) for j in range(m) if grid[i][j]!=0]
    if not non: return [[0]*m for _ in range(n)]
    r0 = min(i for i,_ in non)
    r1 = max(i for i,_ in non)
    c0 = min(j for _,j in non)
    c1 = max(j for _,j in non)
    h = r1-r0+1
    w = c1-c0+1
    M = [row[c0:c1+1] for row in grid[r0:r1+1]]
    vals = {M[i][j] for i in range(h) for j in range(w)}
    rowsU = [i for i in range(h) if all(M[i][j]==M[i][0] for j in range(w))]
    colsU = [j for j in range(w) if all(M[i][j]==M[0][j] for i in range(h))]
    diagU = h==w and all(M[i][i]==M[0][0] for i in range(h))
    anchors = []
    if diagU:
        anchors = [(0,w),(w,0),(2*w,w)]
    elif len(vals)==2:
        anchors = [(0,0),(0,w),(2*w,w)]
    elif len(rowsU)==1:
        r = rowsU[0]
        if r==1:
            anchors = [(2*h,1*w),(2*h,2*w)]
        elif r==2:
            anchors = [(0,0),(1*h,1*w)]
    elif colsU:
        anchors = [(0,0)]
    else:
        anchors = [(0,2*w)]
    out = [[0]*m for _ in range(n)]
    for ro,co in anchors:
        for i in range(h):
            for j in range(w):
                out[ro+i][co+j] = M[i][j]
    return out