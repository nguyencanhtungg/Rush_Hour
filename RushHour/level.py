import vehicles, pickle



# level_1 = vehicles.Vehicles(6)
# level_1.add_vehicle(2, 3, 1)
# level_1.add_vehicle(2, -1,1)
# level_1.add_vehicle(2, 1, 4)
# level_1.add_vehicle(2, -4, 5)
# level_1.add_vehicle(2, -5, 5)
# level_1.add_vehicle(3, -3, 1)
# level_1.add_vehicle(3, 4, 4)
# level_1.add_vehicle(3, 6, 1)

# level_2 = vehicles.Vehicles(6)
# level_2.add_vehicle(2, 3, 2)
# level_2.add_vehicle(2, 5, 5)
# level_2.add_vehicle(2, 6, 5)
# level_2.add_vehicle(3, 1, 1)
# level_2.add_vehicle(3, 4, 1)
# level_2.add_vehicle(3, -5, 1)
# level_2.add_vehicle(2, -3, 5)
# level_2.add_vehicle(2, -4, 4)

# level_99 = vehicles.Vehicles(6)
# level_99.add_vehicle(2,3,4)
# level_99.add_vehicle(2,1,4)
# level_99.add_vehicle(2,4,5)
# level_99.add_vehicle(2,6,5)
# level_99.add_vehicle(2,5,2)
# level_99.add_vehicle(2,-1,5)
# level_99.add_vehicle(3,-3,1)
# level_99.add_vehicle(3,-6,1)
# level_99.add_vehicle(3,-4,4)



levels = {


}

def pop_level():
    global levels
    if len(levels) > 1:
        levels.popitem()
        print("poped last level")

def add_level(level):
    global levels
    levels[len(levels) + 1] = level
    print("added level")

def import_levels_data():
    global levels
    with open("levels_data", 'rb') as lev:
        levels = pickle.load(lev)

def save_levels():
    global levels
    with open("levels_data", 'wb') as lev:
        pickle.dump(levels, lev)


