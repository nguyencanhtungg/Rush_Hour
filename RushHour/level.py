import vehicles



level_1 = vehicles.Vehicles(6)
level_1.add_vehicle(2, 3, 1)
level_1.add_vehicle(2, -1,1)
level_1.add_vehicle(2, 1, 4)
level_1.add_vehicle(2, -4, 5)
level_1.add_vehicle(2, -5, 5)
level_1.add_vehicle(3, -3, 1)
level_1.add_vehicle(3, 4, 4)
level_1.add_vehicle(3, 6, 1)

level_2 = vehicles.Vehicles(6)
level_2.add_vehicle(2, 3, 2)
level_2.add_vehicle(2, 5, 5)
level_2.add_vehicle(2, 6, 5)
level_2.add_vehicle(3, 1, 1)
level_2.add_vehicle(3, 4, 1)
level_2.add_vehicle(3, -5, 1)
level_2.add_vehicle(2, -3, 5)
level_2.add_vehicle(2, -4, 4)







level_99 = vehicles.Vehicles(6)
level_99.add_vehicle(2,3,4)
level_99.add_vehicle(2,1,4)
level_99.add_vehicle(2,4,5)
level_99.add_vehicle(2,6,5)
level_99.add_vehicle(2,5,2)
level_99.add_vehicle(2,-1,5)
level_99.add_vehicle(3,-3,1)
level_99.add_vehicle(3,-6,1)
level_99.add_vehicle(3,-4,4)


levels = {
    1 : level_1,
    2 : level_2
    # "HARDEST" : level_99
}


