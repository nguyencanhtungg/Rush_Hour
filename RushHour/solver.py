import collections, vehicles
import copy

class RushHourSolver:
    def __init__(self, state):
        self.inittial_state = state

    def solver(self):
        initial_state = copy.deepcopy(self.inittial_state)

        queue = collections.deque([(initial_state, [])])

        visited = set()

        while queue:
            current_state, path = queue.popleft()

            current_key_state = self.get_key_state(current_state)

            if current_key_state in visited:
                continue
            visited.add(current_key_state)

            if self.is_goal_state(current_state):
                return path
            
            for vehicle_id in current_state.vehicles.keys():
                for step in [1,-1]:
                    if current_state.check_move_valid(vehicle_id, step):
                        new_state = copy.deepcopy(current_state)
                        new_state.move(vehicle_id, step)

                        queue.append((new_state, path + [(vehicle_id, step)]))

        return None

    def is_goal_state(self, state):
        first_vehicle = state.vehicles[1]
        return first_vehicle.get_pos_last() + first_vehicle.size - 1 == state.size_game
    def get_key_state(self, state):
        state_key = []
        for vehicle_id, vehicle in state.vehicles.items():
            state_key.append((vehicle_id, vehicle.get_pos_last()))
        return tuple(state_key)
    
# TEST SOLVER
state = vehicles.Vehicles(6)
state.add_vehicle(2,3,4)
state.add_vehicle(2,1,4)
state.add_vehicle(2,4,5)
state.add_vehicle(2,6,5)
state.add_vehicle(2,5,2)
state.add_vehicle(2,-1,5)
state.add_vehicle(3,-3,1)
state.add_vehicle(3,-6,1)
state.add_vehicle(3,-4,4)

solver_state = RushHourSolver(state)
solution = solver_state.solver()

if solution == None:
    print("No solution")
else :
    print(len(solution))