def solve(grid):
    H=len(grid); W=len(grid[0])
    vis=[[False]*W for _ in range(H)]
    comps=[]
    for i in range(H):
        for j in range(W):
            if grid[i][j]!=0 and not vis[i][j]:
                col=grid[i][j]
                stack=[(i,j)]; vis[i][j]=True; pix=[]
                while stack:
                    y,x=stack.pop()
                    pix.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0<=ny<H and 0<=nx<W and not vis[ny][nx] and grid[ny][nx]==col:
                            vis[ny][nx]=True
                            stack.append((ny,nx))
                ys=[y for y,_ in pix]; xs=[x for _,x in pix]
                miny,maxy,minx,maxx=min(ys),max(ys),min(xs),max(xs)
                h=maxy-miny+1; w=maxx-minx+1
                area=len(pix)
                is_hollow = (w==h and area==4*w-4)
                comps.append({
                    "pix":pix,"miny":miny,"minx":minx,
                    "h":h,"w":w,"col":col,
                    "hollow":is_hollow
                })
    hollows=[c for c in comps if c["hollow"]]
    crosses=[c for c in comps if not c["hollow"]]
    hollows.sort(key=lambda c:c["minx"])
    crosses.sort(key=lambda c:c["minx"])
    out=[[0]*W for _ in range(H)]
    # pack hollows top-down
    shelves=[]
    for c in hollows:
        placed=False
        for idx,(start,height) in enumerate(shelves):
            if c["h"]<=height:
                y0=start
                ok=True
                for y,x in c["pix"]:
                    ny = y0 + (y - c["miny"])
                    nx = x
                    if out[ny][nx]!=0:
                        ok=False
                        break
                if ok:
                    for y,x in c["pix"]:
                        ny = y0 + (y - c["miny"])
                        out[ny][x]=c["col"]
                    placed=True
                    break
        if not placed:
            # new shelf
            y0 = sum(h for _,h in shelves)
            shelves.append((y0,c["h"]))
            for y,x in c["pix"]:
                ny = y0 + (y - c["miny"])
                out[ny][x]=c["col"]
    # pack crosses bottom-up
    shelves=[]
    for c in crosses:
        placed=False
        for idx,(start,height) in enumerate(shelves):
            if c["h"]<=height:
                y0=start
                ok=True
                for y,x in c["pix"]:
                    ny = y0 + (y - c["miny"])
                    nx = x
                    if out[ny][nx]!=0:
                        ok=False
                        break
                if ok:
                    for y,x in c["pix"]:
                        ny = y0 + (y - c["miny"])
                        out[ny][x]=c["col"]
                    placed=True
                    break
        if not placed:
            y0 = H - c["h"] - sum(h for _,h in shelves)
            shelves.append((y0,c["h"]))
            for y,x in c["pix"]:
                ny = y0 + (y - c["miny"])
                out[ny][x]=c["col"]
    return out