def solve(grid):
    H=len(grid);W=len(grid[0])
    def gcd(a,b):
        while b:b,a=b,a%b
        return a
    nzr=sum(1 for i in range(H) if sum(1 for v in grid[i] if v!=0)>=2)
    nzc=sum(1 for j in range(W) if sum(1 for i in range(H) if grid[i][j]!=0)>=2)
    out=[[0]*W for _ in range(H)]
    if nzr>nzc:
        for i in range(H):
            pos=[j for j in range(W) if grid[i][j]!=0]
            if len(pos)<2: continue
            cnt={}
            for j in pos:
                cnt[grid[i][j]]=cnt.get(grid[i][j],0)+1
            items=sorted(cnt.items(),key=lambda x:-x[1])
            A=items[0][0]
            B=None
            if len(items)>1:
                B=items[-1][0]
            posA=[j for j in pos if grid[i][j]==A]
            posA.sort()
            step=posA[1]-posA[0] if len(posA)>1 else 1
            for k in range(2,len(posA)):
                step=gcd(step,posA[k]-posA[k-1])
            r=posA[0]%step
            if B is not None:
                posB=[j for j in pos if grid[i][j]==B][0]
                if posB%step==r:
                    fillC=B
                    start=min(posA[0],posB);end=max(posA[-1],posB)
                else:
                    fillC=A
                    start=0;end=W-1
            else:
                fillC=A
                start=0;end=W-1
            for j in range(start,end+1):
                if j%step==r:
                    out[i][j]=fillC
    else:
        for j in range(W):
            pos=[i for i in range(H) if grid[i][j]!=0]
            if len(pos)<2: continue
            cnt={}
            for i in pos:
                cnt[grid[i][j]]=cnt.get(grid[i][j],0)+1
            items=sorted(cnt.items(),key=lambda x:-x[1])
            A=items[0][0]
            B=None
            if len(items)>1:
                B=items[-1][0]
            posA=[i for i in pos if grid[i][j]==A]
            posA.sort()
            step=posA[1]-posA[0] if len(posA)>1 else 1
            for k in range(2,len(posA)):
                step=gcd(step,posA[k]-posA[k-1])
            r=posA[0]%step
            if B is not None:
                posB=[i for i in pos if grid[i][j]==B][0]
                if posB%step==r:
                    fillC=B
                    start=min(posA[0],posB);end=max(posA[-1],posB)
                else:
                    fillC=A
                    start=0;end=H-1
            else:
                fillC=A
                start=0;end=H-1
            for i in range(start,end+1):
                if i%step==r:
                    out[i][j]=fillC
    return out