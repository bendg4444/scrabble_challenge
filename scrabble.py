import math, random

class Game:
    def __init__(self, player):
        self.player = player
        self.tiles = Bag()
        self.give_player_rack()
        self.player.print_tiles()

    def give_player_rack(self):
        count = 0
        while count < 7:
            tile = random.choice(self.tiles.bag)
            self.player.rack.append(tile)
            self.tiles.bag.remove(tile)
            count += 1

class Player:
    def __init__(self):
        self.rack = []

    def make_rack(self):
        some = []

    def print_tiles(self):
        list = []
        for tile in self.rack:
            list.append(tile.to_string())
        print(list)



#for each letter
class Tile:
    def __init__(self, letter, val):
        self.letter = letter
        self.val = val

    def to_string(self):
        return f"{self.letter}"


class Bag:
    def __init__(self):
        self.all_tiles = []
        self.bag = []
        self.make_tiles_points_list()
        self.fill_bag()
        

    def make_tiles_points_list(self):
        points_1 = list('EAIONRTLSU')
        self.make_tiles_with_points(points_1, 1)
        points_2 = list('DG')
        self.make_tiles_with_points(points_2, 2)
        points_3 = list('BCMP')
        self.make_tiles_with_points(points_3, 3)
        points_4 = list('FHVWY')
        self.make_tiles_with_points(points_4, 4)
        points_5 = list('K')
        self.make_tiles_with_points(points_5, 5)
        points_8 = list('JX')
        self.make_tiles_with_points(points_8, 8)
        points_10 = list('QZ')
        self.make_tiles_with_points(points_10, 10)

    def make_tiles_with_points(self, list, points):
        for letter in list:
            self.all_tiles.append(Tile(letter, points))

    def fill_bag(self):
        for tile in self.all_tiles:
            if(tile.letter == 'E'):
                self.add_x_times(tile, 12)
            if(tile.letter == 'A' or tile.letter == 'I'):
                self.add_x_times(tile, 9)
            if(tile.letter == 'O'):
                self.add_x_times(tile, 8)
            if(tile.letter == 'N' or tile.letter == 'R' or tile.letter == 'T'):
                self.add_x_times(tile, 6)
            if(tile.letter == 'L' or tile.letter == 'S' or tile.letter == 'U' or tile.letter == 'D'):
                self.add_x_times(tile, 4)
            if(tile.letter == 'G'):
                self.add_x_times(tile, 3)
            if(tile.letter == 'B' or tile.letter == 'C' or tile.letter == 'M' or tile.letter == 'P' or
            tile.letter == 'F' or tile.letter == 'H' or tile.letter == 'V' or tile.letter == 'W'
            or tile.letter == 'Y'):
                self.add_x_times(tile, 2)
            if(tile.letter == 'K' or tile.letter == 'J' or tile.letter == 'X' or tile.letter == 'Q'
             or tile.letter == 'Z'):
                 self.add_x_times(tile, 1)

    def add_x_times(self, tile, x):
        count = 0
        while count < x:
            self.bag.append(tile)
            count +=1


ben = Player()
game = Game(ben)

print(len(ben.rack))



