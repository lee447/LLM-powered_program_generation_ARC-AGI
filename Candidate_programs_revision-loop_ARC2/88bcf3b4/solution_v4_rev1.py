import numpy as np
from collections import defaultdict,deque

def solve(grid):
    h,w=len(grid),len(grid[0])
    cells=defaultdict(list)
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0:
                cells[grid[i][j]].append((i,j))
    def bbox(pts):
        rs=[p[0] for p in pts]; cs=[p[1] for p in pts]
        return min(rs),max(rs),min(cs),max(cs)
    stick=None;best=-1
    for c,pts in cells.items():
        r0,r1,c0,c1=bbox(pts)
        if (r0==r1 or c0==c1) and len(pts)>best:
            best,len_pts= len(pts), len(pts)
            best=len(pts);stick=c
    others=[c for c in cells if c!=stick]
    st=set(cells[stick])
    b1=None
    for c in others:
        for p in cells[c]:
            for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (p[0]+d[0],p[1]+d[1]) in st:
                    b1=c;break
            if b1:break
        if b1:break
    b2=[c for c in others if c!=b1][0]
    for p in cells[b1]:
        for d in [(1,0),(-1,0),(0,1),(0,-1)]:
            q=(p[0]+d[0],p[1]+d[1])
            if q in st:
                attach, pivot = p, q
                break
        else: continue
        break
    def rot90cw(pts,piv):
        pr,pc=piv;out=[]
        for r,c in pts:
            dr,dc=r-pr,c-pc
            out.append((pr+dc,pc-dr))
        return out
    def rot90ccw(pts,piv):
        pr,pc=piv;out=[]
        for r,c in pts:
            dr,dc=r-pr,c-pc
            out.append((pr-dc,pc+dr))
        return out
    def choose(attach,piv):
        if piv[0]==attach[0]:
            return 'hor'
        else:
            return 'ver'
    orient = choose(attach,pivot)
    if orient=='ver':
        if attach[1]<pivot[1]:
            b1_new=rot90ccw(cells[b1],pivot)
        else:
            b1_new=rot90cw(cells[b1],pivot)
    else:
        if attach[0]<pivot[0]:
            b1_new=rot90cw(cells[b1],pivot)
        else:
            b1_new=rot90ccw(cells[b1],pivot)
    new=[[0]*w for _ in range(h)]
    for i,j in cells[stick]:
        new[i][j]=stick
    for i,j in cells[b2]:
        new[i][j]=b2
    for i,j in b1_new:
        if 0<=i<h and 0<=j<w:
            new[i][j]=b1
    return new