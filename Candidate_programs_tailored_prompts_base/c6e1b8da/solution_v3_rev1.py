import math
def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import deque
    # flood‐fill to find shapes
    seen = [[False]*w for _ in range(h)]
    shapes = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                col = grid[i][j]
                pts = []
                q = deque([(i,j)])
                seen[i][j] = True
                mnr = mxr = i
                mnc = mxc = j
                while q:
                    r,c0 = q.popleft()
                    pts.append((r,c0))
                    mnr = min(mnr,r); mxr = max(mxr,r)
                    mnc = min(mnc,c0); mxc = max(mxc,c0)
                    for dr,dc in dirs:
                        rr,cc = r+dr,c0+dc
                        if 0<=rr<h and 0<=cc<w and not seen[rr][cc] and grid[rr][cc]==col:
                            seen[rr][cc]=True
                            q.append((rr,cc))
                cen_r = (mnr+mxr)/2
                cen_c = (mnc+mxc)/2
                shapes.append({'color':col,'pts':pts,'mnr':mnr,'mxr':mxr,'mnc':mnc,'mxc':mxc,'cen':(cen_r,cen_c)})
    # pick anchor color 3
    anchor = next(s for s in shapes if s['color']==3)
    others = [s for s in shapes if s is not anchor]
    # compute angle around anchor
    ac_r,ac_c = anchor['cen']
    def angle(s):
        dy = s['cen'][0]-ac_r
        dx = s['cen'][1]-ac_c
        return math.degrees(math.atan2(dy,dx))
    # we want order left(180), up(90), right(0), down(-90)
    # map angles into bins
    def sector(a):
        if -45<=a<45: return 2  # right
        if 45<=a<135: return 1  # down
        if a>=135 or a< -135: return 0  # left
        return 3  # up
    others.sort(key=lambda s: sector(angle(s)))
    # placement
    out = [[0]*w for _ in range(h)]
    for (r,c0) in anchor['pts']:
        out[r][c0] = 3
    mnr0,mxr0,mnc0,mxc0 = anchor['mnr'],anchor['mxr'],anchor['mnc'],anchor['mxc']
    for s in others:
        if sector(angle(s))==0:  # left
            dx = mnc0 - s['mxc'] - 1
            dy = int((ac_r - s['cen'][0]))
        elif sector(angle(s))==1:  # down
            dy = mxr0 - s['mnr'] + 1
            dx = int((ac_c - s['cen'][1]))
        elif sector(angle(s))==2:  # right
            dx = mxc0 - s['mnc'] + 1
            dy = int((ac_r - s['cen'][0]))
        else:  # up
            dy = mnr0 - s['mxr'] - 1
            dx = int((ac_c - s['cen'][1]))
        for (r,c0) in s['pts']:
            out[r+dy][c0+dx] = s['color']
        # update anchor bbox
        mnr0 = min(mnr0, s['mnr']+dy)
        mnc0 = min(mnc0, s['mnc']+dx)
        mxr0 = max(mxr0, s['mxr']+dy)
        mxc0 = max(mxc0, s['mxc']+dx)
    return out