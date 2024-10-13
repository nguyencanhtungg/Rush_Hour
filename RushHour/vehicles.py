import vehicle

class Vehicles:
    def __init__(self, size_game):
        self.vehicles = {

        }
        self.size_game = size_game
        self.cells = [[0] * size_game for _ in range(size_game)]



    def add_vehicle(self, size,versus,initial):
        self.vehicles[len(self.vehicles) + 1] = vehicle.Vehicle(size,versus,initial)
        if versus > 0:
            for col in range(initial - 1, initial + size - 1):
                self.cells[versus - 1][col] = len(self.vehicles)
        else:
            for row in range(initial - 1, initial + size - 1):
                self.cells[row][-versus - 1] = len(self.vehicles)

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
    