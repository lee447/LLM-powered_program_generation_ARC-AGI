import numpy as np
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0]) if grid else 0
    arr = np.array(grid)
    r5, c5 = np.where(arr==5)
    r0, c0 = r5.min(), c5.min()
    r1, c1 = r5.max(), c5.max()
    out = arr.copy()
    def drop_row(r):
        cs = np.where((arr[r]!=0)&(arr[r]!=5))[0]
        if cs.size>1:
            out[r,cs.max()]=0
        elif cs.size==1:
            out[r,cs[0]]=0
    def drop_col(c):
        rs = np.where((arr[:,c]!=0)&(arr[:,c]!=5))[0]
        if rs.size>1:
            out[rs.max(),c]=0
        elif rs.size==1:
            out[rs[0],c]=0
    for d in [1,-1]:
        for k in range(1, max(h,w)):
            if r1 + d*k*4 < h and r1 + d*k*4 >= 0:
                drop_row(r1 + d*k*4)
            if r0 + d*k*4 < h and r0 + d*k*4 >= 0:
                drop_row(r0 + d*k*4)
            if c1 + d*k*4 < w and c1 + d*k*4 >= 0:
                drop_col(c1 + d*k*4)
            if c0 + d*k*4 < w and c0 + d*k*4 >= 0:
                drop_col(c0 + d*k*4)
    return out.tolist()