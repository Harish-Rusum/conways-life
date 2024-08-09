class Grid:
    def __init__(self, x, y):
        self.grid = [["d"] * x for _ in range(y)]
    
    def flip(self, x, y):
        if self.grid[y][x] == "d":
            self.grid[y][x] = "l"
        else:
            self.grid[y][x] = "d"

    def update(self):
        copy = [row[:] for row in self.grid]
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                neighbors = 0
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(self.grid[0]) and 0 <= ny < len(self.grid):
                        if self.grid[ny][nx] == "l":
                            neighbors += 1
                
                if self.grid[y][x] == "l":
                    if neighbors < 2 or neighbors > 3:
                        copy[y][x] = "d"
                else:
                    if neighbors == 3:
                        copy[y][x] = "l"
        
        self.grid = copy

