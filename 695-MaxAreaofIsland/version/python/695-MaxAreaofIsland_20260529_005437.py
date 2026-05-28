# Last updated: 5/29/2026, 12:54:37 AM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        def dfs(ri,ci):
            if ri<0 or ci<0 or ri>=rows or ci>=cols or grid[ri][ci]==0:
                return 0
            grid[ri][ci]=0
            return 1+dfs(ri,ci+1)+dfs(ri,ci-1)+dfs(ri+1,ci)+dfs(ri-1,ci)
        max_area=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    area=dfs(i,j)
                    if max_area<area:
                        max_area=area
        return max_area
        
        