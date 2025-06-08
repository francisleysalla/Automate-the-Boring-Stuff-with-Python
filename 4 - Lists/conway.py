import time, random, copy
width = 50
height = 50
options = [" ", "#"]
grid = []
times = 0

# Create a random grid
for i in range(height):
    row = []
    for j in range(width):
        row.append(random.choice(options))
    grid.append(row)


# Create a loop to update the grid
while True:
    # Print the grid
    for row in grid:
        print(" ".join(cell for cell in row))
    # time.sleep(1)
    print('\n\n\n\n')
    # Living has 2 or 3 living neighbours, it stays alive
    # Dead has exactly 3 living neighbours, it becomes alive
    updated_grid = copy.deepcopy(grid)
    for row_index, row in enumerate(grid):
        for item_index, item  in enumerate(row):
            living_neighbours = 0
            # Check the 8 neighbours
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i == 0 and j == 0):
                        continue
                    neighbour_x = (row_index + i) % height
                    neighbour_y = (item_index + j) % width
                    if grid[neighbour_x][neighbour_y] == "#":
                        living_neighbours += 1

            # Apply the rules of Conway's Game of Life
            if item == '#':
                if living_neighbours < 2 or living_neighbours > 3:
                    updated_grid[row_index][item_index] = " "
            elif living_neighbours == 3:
                updated_grid[row_index][item_index] = "#"
    
    grid = updated_grid
