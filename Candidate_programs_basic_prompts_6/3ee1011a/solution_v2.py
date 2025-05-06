from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    counts={}
    for r in grid:
        for v in r:
            if v!=0:
                counts[v]=counts.get(v,0)+1
    segments=sorted(counts.items(), key=lambda x:-x[1])
    N=segments[0][1]
    res=[[0]*N for _ in range(N)]
    for layer,(color,_) in enumerate(segments):
        low=layer
        high=N-1-layer
        for j in range(low,high+1):
            res[low][j]=color
            res[high][j]=color
        for i in range(low,high+1):
            res[i][low]=color
            res[i][high]=color
    return res