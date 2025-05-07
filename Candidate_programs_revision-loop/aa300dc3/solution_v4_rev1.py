import sys
def solve(grid):
    m,n=len(grid),len(grid[0])
    zeros=[(i,j) for i in range(m) for j in range(n) if grid[i][j]==0]
    zeros.sort()
    zero_set=set(zeros)
    best_chain=[]
    for dr,dc in ((1,1),(1,-1)):
        for i,j in zeros:
            if (i-dr,j-dc) not in zero_set and (i+dr,j+dc) in zero_set:
                chain=[(i,j)]
                x,y=i,j
                while (x+dr,y+dc) in zero_set:
                    x+=dr; y+=dc; chain.append((x,y))
                if len(chain)>len(best_chain):
                    best_chain=chain
    out=[row[:] for row in grid]
    for i,j in best_chain:
        out[i][j]=8
    return out

if __name__=='__main__':
    data=sys.stdin.read().strip().split()
    h,w=map(int,data[:2]); vals=list(map(int,data[2:]))
    grid=[vals[i*w:(i+1)*w] for i in range(h)]
    res=solve(grid)
    for row in res: print(' '.join(map(str,row)))