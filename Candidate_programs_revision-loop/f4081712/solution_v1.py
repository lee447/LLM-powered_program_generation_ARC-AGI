from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    rmin, rmax, cmin, cmax = H, -1, W, -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 3:
                if i < rmin: rmin = i
                if i > rmax: rmax = i
                if j < cmin: cmin = j
                if j > cmax: cmax = j
    h, w = rmax - rmin + 1, cmax - cmin + 1
    out = [[0]*w for _ in range(h)]
    def mode(lst):
        cnt = {}
        for x in lst:
            cnt[x] = cnt.get(x,0)+1
        best = None
        mb = -1
        for x,v in cnt.items():
            if v>mb:
                mb=v; best=x
        return best
    for i in range(h):
        for j in range(w):
            if i==0 and rmin>0 and grid[rmin-1][cmin+j]!=3:
                out[i][j] = grid[rmin-1][cmin+j]
            elif i==h-1 and rmax+1<H and grid[rmax+1][cmin+j]!=3:
                out[i][j] = grid[rmax+1][cmin+j]
            elif j==0 and cmin>0 and grid[rmin+i][cmin-1]!=3:
                out[i][j] = grid[rmin+i][cmin-1]
            elif j==w-1 and cmax+1<W and grid[rmin+i][cmax+1]!=3:
                out[i][j] = grid[rmin+i][cmax+1]
            else:
                nbr = []
                if rmin>0 and grid[rmin-1][cmin+j]!=3:
                    nbr.append(grid[rmin-1][cmin+j])
                if rmax+1<H and grid[rmax+1][cmin+j]!=3:
                    nbr.append(grid[rmax+1][cmin+j])
                if cmin>0 and grid[rmin+i][cmin-1]!=3:
                    nbr.append(grid[rmin+i][cmin-1])
                if cmax+1<W and grid[rmin+i][cmax+1]!=3:
                    nbr.append(grid[rmin+i][cmax+1])
                out[i][j] = mode(nbr) if nbr else 0
    return out