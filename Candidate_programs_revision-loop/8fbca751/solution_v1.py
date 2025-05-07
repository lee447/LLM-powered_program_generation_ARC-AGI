def solve(grid):
    h=len(grid); w=len(grid[0])
    seen=[[False]*w for _ in range(h)]
    boxes=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==8 and not seen[i][j]:
                seen[i][j]=True
                stack=[(i,j)]
                minr,maxr,minc,maxc=i,i,j,j
                while stack:
                    r,c=stack.pop()
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==8:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                            minr=min(minr,nr); maxr=max(maxr,nr)
                            minc=min(minc,nc); maxc=max(maxc,nc)
                boxes.append([minr,maxr,minc,maxc])
    changed=True
    while changed:
        changed=False
        n=len(boxes)
        for i in range(n):
            for j in range(i+1,n):
                if boxes[i][2] <= boxes[j][3] and boxes[j][2] <= boxes[i][3]:
                    mi=min(boxes[i][0],boxes[j][0]); ma=max(boxes[i][1],boxes[j][1])
                    mc=min(boxes[i][2],boxes[j][2]); Mx=max(boxes[i][3],boxes[j][3])
                    boxes.pop(j); boxes.pop(i)
                    boxes.append([mi,ma,mc,Mx])
                    changed=True
                    break
            if changed: break
    out=[row[:] for row in grid]
    for minr,maxr,minc,maxc in boxes:
        for r in range(minr,maxr+1):
            for c in range(minc,maxc+1):
                if out[r][c]==0:
                    out[r][c]=2
    return out