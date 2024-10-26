import vehicle, solver


class Vehicles:
    def __init__(self, size_game):
        self.vehicles = {

        }
        self.size_game = size_game
        self.moved = []
        self.cells = [[0] * size_game for _ in range(size_game)]



    def add_vehicle(self, size,versus,initial):
        if self.check_add_vehicle_valid(size, versus, initial):
            self.vehicles[len(self.vehicles) + 1] = vehicle.Vehicle(size,versus,initial)
        self.update_cells()

    def check_add_vehicle_valid(self, size, versus, initial):
        if not (0 <= abs(versus) <= self.size_game and 0 <= initial <= self.size_game and abs(initial) + size - 1 <= self.size_game):
            return False
        if versus > 0:
            for col in range(initial, initial + size):
                if self.cells[versus - 1][col - 1] != 0:
                    return False
            return True
        else:
            for row in range(initial, initial + size ):
                if self.cells[row - 1][-versus - 1] != 0:
                    return False
            return True
    def len(self):
        return len(self.vehicles)

    def get_vehicle(self, index):
        return self.vehicles.get(index)
    
    def check_move_valid(self, vehicle, step):
        pos_last = self.vehicles[vehicle].get_pos_last()
        size_vehicle = self.vehicles[vehicle].size
        versus_vehicle = self.vehicles[vehicle].versus
        
        if versus_vehicle > 0:
            if step > 0:
                if pos_last + size_vehicle - 1 + step > self.size_game:
                    return False
                for col_cell in range(pos_last + size_vehicle, pos_last + size_vehicle + step):
                    if not self.cells[versus_vehicle - 1][col_cell - 1] == 0:
                        return False
                return True
            else:
                if pos_last + step < 1:
                    return False
                for col_cell in range(pos_last + step, pos_last):
                    if not self.cells[versus_vehicle - 1][col_cell - 1] == 0:
                        return False
                return True
        else :
            if step > 0:
                if pos_last + size_vehicle - 1 + step > self.size_game:
                    return False
                for row_cell in range(pos_last + size_vehicle, pos_last + size_vehicle + step):
                    if not self.cells[row_cell - 1][-versus_vehicle - 1] == 0:
                        return False
                return True
            else :
                if pos_last + step < 1:
                    return False
                for row_cell in range(pos_last + step, pos_last):
                    if not self.cells[row_cell - 1][-versus_vehicle - 1] == 0:
                        return False
                return True

    def move(self,vehicle, step):
        if self.check_move_valid(vehicle, step):
            self.vehicles[vehicle].add_move(step)
            self.moved.append(vehicle)
            self.update_cells()

    def update_cells(self):
        self.cells = [[0] * self.size_game for _ in range(self.size_game)]
        for vehicle_name in self.vehicles.keys():
            vehicle = self.vehicles.get(vehicle_name)
            if vehicle.versus > 0:
                for col_cell in range(vehicle.get_pos_last(), vehicle.get_pos_last() + vehicle.size):
                    self.cells[vehicle.versus - 1][col_cell - 1] = vehicle_name
            else :
                for row_cell in range(vehicle.get_pos_last(), vehicle.get_pos_last() + vehicle.size):
                    self.cells[row_cell - 1][-vehicle.versus - 1] = vehicle_name

    #reset
    def restart_game(self):
        for vehicle in self.vehicles.values():
            vehicle.reset_vehicle()
        self.update_cells()

    def reset_game(self):
        self.vehicles.clear()
        self.update_cells()

    def pop_last_vehicle(self):
        if len(self.vehicles) > 0:
            self.vehicles.popitem()

    def back_move(self):
        if len(self.moved) > 0:
            self.vehicles[self.moved.pop()].back_move()
            self.update_cells()

    def solve(self):
        solver.solve(self)

    