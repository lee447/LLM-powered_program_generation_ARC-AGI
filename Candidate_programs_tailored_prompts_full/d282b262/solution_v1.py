def solve(grid):
    h=len(grid); w=len(grid[0])
    out=[[0]*w for _ in range(h)]
    for i,row in enumerate(grid):
        runs=[]
        j=0
        while j<w:
            if row[j]==0:
                j+=1
            else:
                run=[]
                while j<w and row[j]!=0:
                    run.append(row[j]); j+=1
                runs.append(run)
        total=sum(len(r) for r in runs)
        start=w-total
        for run in runs:
            for v in run:
                out[i][start]=v; start+=1
    return out