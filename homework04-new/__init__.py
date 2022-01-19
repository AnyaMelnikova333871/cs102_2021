
'''
y, x = cell
ans = []
if 0 < x < len(self.grid[0]) - 1 and 0 < y < len(self.grid) - 1:
    for i in (-1, 0, 1):


        for j in (-1, 0, 1):
        ans.append(self.grid[y + i][x + j])
    del ans[4]
if x == 0 and y == 0:  # upper left
    ans = [self.grid[y][x + 1], self.grid[y + 1][x], self.grid[y + 1][x + 1]]
if x == 0 and y == len(self.grid) - 1:  # lower left
    ans = [self.grid[y][x + 1], self.grid[y - 1][x], self.grid[y - 1][x + 1]]
if x == len(self.grid[0]) - 1 and y == 0:  # upper right
    ans = [self.grid[y][x - 1], self.grid[y + 1][x], self.grid[y + 1][x - 1]]
if x == len(self.grid[0]) - 1 and y == len(self.grid) - 1:  # lower right
    ans = [self.grid[y][x - 1], self.grid[y - 1][x], self.grid[y - 1][x - 1]]
if x == 0 and 0 < y < len(self.grid) - 1:  # left side
    ans = [self.grid[y][x + 1], self.grid[y + 1][x], self.grid[y + 1][x + 1], self.grid[y][x + 1],
           self.grid[y - 1][x + 1]]
if x == len(self.grid[0]) - 1 and 0 < y < len(self.grid) - 1:  # right side
    ans = [self.grid[y][x - 1], self.grid[y + 1][x], self.grid[y + 1][x - 1], self.grid[y - 1][x],
           self.grid[y - 1][x - 1]]
if 0 < x < len(self.grid[0]) - 1 and y == 0:  # upper side
    ans = [self.grid[y][x + 1], self.grid[y + 1][x], self.grid[y + 1][x + 1], self.grid[y][x - 1],
           self.grid[y + 1][x - 1]]
if 0 < x < len(self.grid[0]) - 1 and y == len(self.grid) - 1:  # lower side
    ans = [self.grid[y][x + 1], self.grid[y - 1][x], self.grid[y - 1][x + 1], self.grid[y][x - 1],
           self.grid[y - 1][x - 1]]
return ans
'''