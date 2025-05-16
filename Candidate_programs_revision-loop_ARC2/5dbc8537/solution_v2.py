from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    # find uniform rows and cols
    uniform_rows = [r for r in range(h) if len({grid[r][c] for c in range(w)}) == 1]
    uniform_cols = [c for c in range(w) if len({grid[r][c] for r in range(h)}) == 1]
    def flood(x0,y0,seen):
        col = grid[y0][x0]
        stack = [(x0,y0)]
        comp = []
        while stack:
            x,y = stack.pop()
            if (x,y) in seen: continue
            if grid[y][x]!=col: continue
            seen.add((x,y))
            comp.append((x,y))
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny = x+dx, y+dy
                if 0<=nx<w and 0<=ny<h:
                    stack.append((nx,ny))
        return comp
    if len(uniform_cols) > 1:
        # vertical sep mode
        seps = sorted(uniform_cols)
        left_border, sep = seps[0], seps[1]
        x0, x1 = left_border+1, sep
        region_w = x1 - x0
        sep_col = grid[0][sep]
        bg = max(set(sum(grid,[])), key=sum([row.count(row[0]) for row in grid]))
        # init output
        out = [[sep_col if c in (0,region_w+1) else bg for c in range(region_w+2)] for _ in range(h)]
        out = [[sep_col] + [bg]*region_w + [sep_col] for _ in range(h)]
        # find shapes to right of sep
        seen = set()
        comps = []
        for y in range(h):
            for x in range(sep+1,w):
                if (x,y) not in seen and grid[y][x]!=bg and grid[y][x]!=sep_col:
                    comp = flood(x,y,seen)
                    xs = [p[0] for p in comp]; ys = [p[1] for p in comp]
                    comps.append((min(ys),min(xs),comp))
        comps.sort()
        cur_y = 0
        for _,_,comp in comps:
            xs = [p[0] for p in comp] if False else None
            ys = [p[1] for p in comp] if False else None
        # better track each comp with its bbox
        structured = []
        for _,_,comp in comps:
            cols = [p[0] for p in comp]; rows = [p[1] for p in comp]
            minx,maxx = min(cols), max(cols)
            miny,maxy = min(rows), max(rows)
            structured.append((miny,minx,maxy-miny+1,maxx-minx+1,comp))
        cur_y = 0
        for miny, minx, h_s, w_s, comp in structured:
            off_x = (region_w - w_s)//2
            for x,y in comp:
                out[cur_y + (y-miny)][1 + off_x + (x-minx)] = grid[y][x]
            cur_y += h_s
        return out
    else:
        # horizontal sep mode
        seps = sorted(uniform_rows)
        top_border, sep = seps[0], seps[1]
        y0, y1 = top_border+1, sep
        region_h = y1 - y0
        sep_row = grid[sep][0]
        bg = max(set(sum(grid,[])), key=lambda c: sum(row.count(c) for row in grid))
        out = [[sep_row if r in (0,region_h+1) else bg for _ in range(w)] for r in range(region_h+2)]
        # find shapes below sep
        seen = set()
        comps = []
        for y in range(sep+1,h):
            for x in range(w):
                if (x,y) not in seen and grid[y][x]!=bg and grid[y][x]!=sep_row:
                    comp = flood(x,y,seen)
                    xs = [p[0] for p in comp]; ys = [p[1] for p in comp]
                    comps.append((min(xs),min(ys),comp))
        comps.sort()
        structured = []
        for _,_,comp in comps:
            cols = [p[0] for p in comp]; rows = [p[1] for p in comp]
            minx,maxx = min(cols), max(cols)
            miny,maxy = min(rows), max(rows)
            structured.append((minx,miny,maxx-minx+1,maxy-miny+1,comp))
        cur_x = 0
        for minx, miny, w_s, h_s, comp in structured:
            off_y = (region_h - h_s)//2
            for x,y in comp:
                out[1 + off_y + (y-miny)][cur_x + (x-minx)] = grid[y][x]
            cur_x += w_s
        return out