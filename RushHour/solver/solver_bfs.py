from collections import deque

class RushHour:
    def __init__(self, grid, target_car, exit_col):
        self.grid = grid  # ma trận lưới của trò chơi
        self.target_car = target_car  # xe cần thoát (ví dụ: 'R' cho xe màu đỏ)
        self.exit_col = exit_col  # cột của lối ra
    
    def is_goal(self, grid):
        # Kiểm tra nếu xe mục tiêu đã ở lối ra
        target_row = None
        for row in range(len(grid)):
            if self.target_car in grid[row]:
                target_row = row
                break
        return grid[target_row][self.exit_col] == self.target_car
    
    def get_neighbors(self, grid):
        # Tạo ra các trạng thái hợp lệ tiếp theo (lân cận)
        neighbors = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                car = grid[row][col]
                if car != '.' and car != self.target_car:  # Bỏ qua ô trống và xe mục tiêu
                    # Nếu xe có thể di chuyển
                    if self.can_move_horizontally(grid, row, col):
                        # Tạo các trạng thái khi xe di chuyển ngang
                        neighbors += self.move_horizontally(grid, row, col, car)
                    if self.can_move_vertically(grid, row, col):
                        # Tạo các trạng thái khi xe di chuyển dọc
                        neighbors += self.move_vertically(grid, row, col, car)
        return neighbors
    
    def can_move_horizontally(self, grid, row, col):
        # Kiểm tra nếu xe có thể di chuyển ngang
        return col < len(grid[0]) - 1 and grid[row][col] == grid[row][col + 1]

    def can_move_vertically(self, grid, row, col):
        # Kiểm tra nếu xe có thể di chuyển dọc
        return row < len(grid) - 1 and grid[row][col] == grid[row + 1][col]

    def move_horizontally(self, grid, row, col, car):
        # Trả về các trạng thái lưới sau khi xe di chuyển ngang
        new_states = []
        # Di chuyển sang trái
        if col > 0 and grid[row][col - 1] == '.':
            new_grid = [list(r) for r in grid]
            new_grid[row][col - 1], new_grid[row][col] = new_grid[row][col], '.'
            new_states.append(new_grid)
        # Di chuyển sang phải
        if col < len(grid[0]) - 1 and grid[row][col + 1] == '.':
            new_grid = [list(r) for r in grid]
            new_grid[row][col + 1], new_grid[row][col] = new_grid[row][col], '.'
            new_states.append(new_grid)
        return new_states

    def move_vertically(self, grid, row, col, car):
        # Trả về các trạng thái lưới sau khi xe di chuyển dọc
        new_states = []
        # Di chuyển lên
        if row > 0 and grid[row - 1][col] == '.':
            new_grid = [list(r) for r in grid]
            new_grid[row - 1][col], new_grid[row][col] = new_grid[row][col], '.'
            new_states.append(new_grid)
        # Di chuyển xuống
        if row < len(grid) - 1 and grid[row + 1][col] == '.':
            new_grid = [list(r) for r in grid]
            new_grid[row + 1][col], new_grid[row][col] = new_grid[row][col], '.'
            new_states.append(new_grid)
        return new_states

    def solve(self):
        # Thuật toán BFS để tìm giải pháp
        queue = deque([self.grid])
        visited = set()
        visited.add(tuple(tuple(row) for row in self.grid))  # Chuyển grid thành tuple để lưu trong visited
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                current_grid = queue.popleft()
                if self.is_goal(current_grid):
                    print(f"Solved in {steps} steps")
                    return steps
                
                # Lấy các trạng thái lân cận
                for neighbor in self.get_neighbors(current_grid):
                    neighbor_tuple = tuple(tuple(row) for row in neighbor)
                    if neighbor_tuple not in visited:
                        visited.add(neighbor_tuple)
                        queue.append(neighbor)
            steps += 1
        print("No solution found")
        return -1


# Ví dụ trò chơi Rush Hour
# . là ô trống, 'R' là xe mục tiêu (xe màu đỏ)
grid = [
    ['.', '.', '.', 'A', 'A', '.'],
    ['.', 'R', 'R', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['C', 'C', 'D', '.', '.', '.'],
    ['.', '.', 'D', '.', '.', '.'],
    ['E', 'E', 'F', 'F', '.', '.']
]

target_car = 'R'  # Xe cần thoát
exit_col = 5  # Cột thoát (đích)

# Khởi tạo trò chơi và giải
game = RushHour(grid, target_car, exit_col)
game.solve()
