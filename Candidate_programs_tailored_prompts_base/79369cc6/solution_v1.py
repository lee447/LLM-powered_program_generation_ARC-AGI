def solve(grid):
    h,len_row= len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def find_clusters(color):
        visited=set()
        clusters=[]
        for i in range(h):
            for j in range(len_row):
                if grid[i][j]==color and (i,j) not in visited:
                    stack=[(i,j)]
                    comp=[]
                    visited.add((i,j))
                    while stack:
                        x,y=stack.pop()
                        comp.append((x,y))
                        for dx,dy in dirs:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<h and 0<=ny<len_row and grid[nx][ny]==color and (nx,ny) not in visited:
                                visited.add((nx,ny))
                                stack.append((nx,ny))
                    clusters.append(comp)
        return clusters
    grey_clusters = find_clusters(4)
    def cluster_key(c):
        return (min(r for r,_ in c), min(c for _,c in c))
    anchor = min(grey_clusters, key=cluster_key)
    min_ar, min_ac = min(r for r,_ in anchor), min(c for _,c in anchor)
    anchor_offsets = [(r-min_ar, c-min_ac) for r,c in anchor]
    def variants(offsets):
        vs=set()
        for _ in range(4):
            offsets=[(c, -r) for r,c in offsets]
            for flip in (False,True):
                arr=[(r, -c) if flip else (r, c) for r,c in offsets]
                mr,mc=min(r for r,_ in arr), min(c for _,c in arr)
                norm=tuple(sorted((r-mr,c-mc) for r,c in arr))
                vs.add(norm)
        return vs
    shape_vars = variants(anchor_offsets)
    pink_clusters = find_clusters(6)
    for comp in pink_clusters:
        mr,mc = min(r for r,_ in comp), min(c for _,c in comp)
        norm=tuple(sorted((r-mr,c-mc) for r,c in comp))
        if norm in shape_vars:
            for r,c in comp:
                grid[r][c]=4
    return grid