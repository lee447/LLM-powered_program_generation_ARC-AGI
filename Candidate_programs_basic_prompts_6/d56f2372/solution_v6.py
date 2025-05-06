from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid); w=len(grid[0])
    clusters={}
    for y in range(h):
        for x in range(w):
            c=grid[y][x]
            if c>0:
                if c not in clusters:
                    clusters[c]=[x,x,y,y,0]
                info=clusters[c]
                info[0]=min(info[0],x)
                info[1]=max(info[1],x)
                info[2]=min(info[2],y)
                info[3]=max(info[3],y)
                info[4]+=1
    best=None; best_area=-1
    for c,(xmin,xmax,ymin,ymax,count) in clusters.items():
        area=(xmax-xmin+1)*(ymax-ymin+1)
        holes=area-count
        if holes>=count and area>best_area:
            best_area=area; best=(c,xmin,xmax,ymin,ymax)
    if best is None:
        return [[]]
    c,xmin,xmax,ymin,ymax=best
    out=[]
    for y in range(ymin,ymax+1):
        row=[]
        for x in range(xmin,xmax+1):
            row.append(c if grid[y][x]==c else 0)
        out.append(row)
    return out