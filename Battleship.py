class ShipBoard:
    def __init__(self):

        self.squares = []
        self.remain = [False * 100]
        self.ships = [] #(x, y, length, dir)

        for i in range(100):s
            a, b = i//10, i%10
            self.squares.append(Square(a, b, "ship"))


    def check_legal_placement(self, x, y, length, dir):
        pass
        # TODO: check <length> squares from (x, y) in direction: <dir>

    def place_ship(self, x, y, length, dir):
        pass
        # TODO: call check_legal_placement
        # TODO: place <length> squares from (x, y) in direction: <dir>

    def check_if_ship(self, x, y):
        pass
        # TODO: check if (x, y) has a ship

    def check_remaining_ship(self):
        pass
        # TODO: check each squares of 5 ships

    def destroy(self, x, y):
        pass
        # TODO: change the square (x, y)
    
    def restore(self):
        pass
        # TODO: revert all changes

    def print_board(self):
        pass
        # TODO: print out the ship board

class AtkBoard:
    def __init__(self):

        self.squares = []
        self.legal = [True*100]

        for _ in range(100):
            a, b = i//10, i%10
            self.squares.append(Square(a, b, "atk"))

    def shoot(self, x, y, val):
        pass
        # TODO: change the square (x, y) that is <hit/missed>

class Square:
    def __init__(self, r, c, t):
        self.row = r
        self.col = c
        self.state = True # True if intact, False if targeted
        self.type = t # "ship" if ship_square, "atk" if atk_square
        self.content = "-" # "-" if nothing, "o" if ship, "x" if shot
        self.color = "#ffffff" # White if normal, Red if hit, Gray if shot/miss, respective color for ship
        # White: #ffffff
        # Gray: #a6a6a6
        # Red: #ff0000
        # Yellow (ship-5): #ffff00
        # Green (ship-4): #7cfc00
        # Light Blue (ship-3-1): #00bfff
        # Dark Blue (ship-3-2): #0000ff
        # Orange (ship-2): #ffa500

    def chosen_for_attack(self, val):
        pass
        # TODO: change state, content, color

    def chosen_for_shot(self):
        pass
        # TODO: change state, color
