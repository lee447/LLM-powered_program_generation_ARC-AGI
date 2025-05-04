def solve(grid):
    h=len(grid); w=len(grid[0])
    coords=[(y,x) for y in range(h) for x in range(w) if grid[y][x]!=0]
    if not coords:
        return [row[:] for row in grid]
    ys=[y for y,x in coords]; xs=[x for y,x in coords]
    min_y,min_x,min_x = min(ys),min(xs),min(xs)
    max_y,max_x = max(ys),max(xs)
    def is_horiz():
        s=min_y+max_y
        for y,x in coords:
            y2=s-y
            if y2<0 or y2>=h or grid[y2][x]!=grid[y][x]:
                return False
        return True
    horiz=is_horiz()
    res=[row[:] for row in grid]
    if horiz:
        axis=(min_y+max_y+1)//2
        for x in range(w): res[axis][x]=3
    else:
        s=min_x+max_x
        axis=(s+1)//2
        for y in range(h): res[y][axis]=3
    return res