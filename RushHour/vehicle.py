class Vehicle:
    def __init__(self, size, versus, initial):
        self.size = size
        self.versus = versus
        self.initial = initial
        self.pos = [-999999, initial]
        self.moves = [-999999]


    def add_pos(self, position) :
        self.pos.append(position)

    def get_pos(self, index):
        return self.pos[index]
    def get_pos_last(self):
        return self.get_pos(len(self.pos) - 1)
    
    def add_move(self, move):
       self.pos.append(self.pos[len(self.pos) - 1] + move)
       self.moves.append(move)
    
    def get_move(self, index):
        return self.moves[index]
    
    def reset_vehicle(self):
        self.pos = [-999999, self.initial]
        self.moves = [-999999]

    def back_move(self):
        if len(self.moves) > 1:
            self.moves.pop()
            self.pos.pop()




