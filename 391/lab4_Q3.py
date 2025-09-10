import heapq

class Solution():
    def getShortestPath(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        pq = []
        pq.append((0, 0, 0, False)) # path length, r, c, has_broken
        visit = {(0, 0, False)} #r,c,flag

        while pq:
            path_len, row, col, is_broken = heapq.heappop(pq)
            if row == ROWS-1 and col == COLS-1:
                return path_len
            nei = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)] 
            for nr, nc in nei:
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc, is_broken) not in visit:
                    visit.add((nr, nc, is_broken))
                    if not is_broken and grid[nr][nc] == 1:
                        heapq.heappush(pq, (path_len+1, nr, nc, True))
                    if grid[nr][nc] == 1:
                        continue
                    heapq.heappush(pq, (path_len+1, nr, nc, is_broken))
        return -1    
    
if __name__ == "__main__":
    grid = [[0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 1],
            [1, 1, 1, 0]]
    s = Solution()
    shortest = s.getShortestPath(grid)
    print(shortest)