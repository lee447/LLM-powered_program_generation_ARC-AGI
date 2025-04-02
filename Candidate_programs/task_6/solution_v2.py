from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    r = len(grid)
    c = len(grid[0]) if r else 0
    res = [None]*r
    is_sep = [all(x==0 for x in grid[i]) for i in range(r)]
    blocks = []
    i = 0
    while i < r:
        typ = is_sep[i]
        start = i
        while i < r and is_sep[i]==typ:
            i += 1
        end = i-1
        blocks.append((typ, start, end))
    def process_pattern_row(row):
        new_row = row[:]
        j = 0
        while j < c:
            if new_row[j] == 0:
                start_j = j
                while j < c and new_row[j] == 0:
                    j += 1
                end_j = j-1
                if start_j > 0 and end_j < c-1:
                    for k in range(start_j, j):
                        new_row[k] = 2
            else:
                j += 1
        return new_row
    def leading_zeros(row):
        cnt = 0
        for x in row:
            if x==0:
                cnt += 1
            else:
                break
        return cnt
    def trailing_zeros(row):
        cnt = 0
        for x in reversed(row):
            if x==0:
                cnt += 1
            else:
                break
        return cnt
    # Process blocks in order.
    prev_pat_block_end = None
    prev_pat_orig = None
    prev_pat_proc = None
    # Also gather indices of blocks that are patterns.
    for b in blocks:
        typ, start, end = b
        if not typ: # pattern block
            for i in range(start, end+1):
                res[i] = process_pattern_row(grid[i])
            prev_pat_block_end = end
            prev_pat_orig = grid[end][:]
            prev_pat_proc = res[end][:]
        else:  # separator block
            # Determine if this block is intermediate: check if there is a following block and it is pattern.
            idx = blocks.index(b)
            if idx < len(blocks)-1 and (not blocks[idx+1][0]):
                intermediate = True
            else:
                intermediate = False
            if prev_pat_block_end is None:
                # if no previous pattern block, try using next pattern block
                if idx < len(blocks)-1:
                    nxt = blocks[idx+1]
                    dummy = grid[nxt[1]][:]
                else:
                    dummy = [0]*c
                ref_orig = dummy
                ref_proc = dummy
            else:
                ref_orig = prev_pat_orig
                ref_proc = prev_pat_proc
            if intermediate:
                left_margin = leading_zeros(ref_orig)
                right_margin = trailing_zeros(ref_orig)
                for i in range(start, end+1):
                    new_row = []
                    for j in range(c):
                        if j < left_margin or j >= c - right_margin:
                            new_row.append(1)
                        else:
                            new_row.append(2)
                    res[i] = new_row
            else:
                for i in range(start, end+1):
                    new_row = []
                    for j in range(c):
                        if ref_proc[j] == 2:
                            new_row.append(1)
                        else:
                            new_row.append(0)
                    res[i] = new_row
    return res