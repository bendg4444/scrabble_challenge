import math, random

# Sets up and Kicks off the game
class Game:
    def __init__(self, player):
        self.player = player
        self.tiles = Bag()
        self.dict = Words()
        self.give_player_rack()
        self.player.print_tiles()
        self.player.sort_letters()
        self.play_game()

    def play_game(self):
        self.dict.check_match(self.player.letters)
        self.dict.print_matching_words()
        #print(self.dict.matches_index)

    def give_player_rack(self):
        count = 0
        while count < 7:
            tile = random.choice(self.tiles.bag)
            self.player.rack.append(tile)
            self.tiles.bag.remove(tile)
            count += 1

#rack is original tiles [letter + points], letters is just letters
class Player:
    def __init__(self):
        self.rack = []
        self.letters = []

    def print_tiles(self):
        list = []
        for tile in self.rack:
            list.append(tile.to_string())
        print(list)

    def sort_letters(self):
        letters = []
        for tile in self.rack:
            letters.append(tile.letter)
        self.letters = sorted(letters)

    def print_letters(self):
        list = []
        for letter in self.letters:
            list.append(letter)
        print(list)

class Tile:
    def __init__(self, letter, val):
        self.letter = letter
        self.val = val

    def to_string(self):
        return f"{self.letter}"

#fills bag of tiles
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

class Words:
    # original holds the original word list (e.g whole words)
    # words holds the sorted into alphabetical words
    # matches_index will reference original 
    def __init__(self):
        self.original = []
        self.words = []
        self.matches_index = []
        self.read_in_file()
        self.remove_first_ele()

    def read_in_file(self):
        with open('dictionary.txt', 'r') as f:
            for line in f:
                self.original.append(line)
                self.words.append(sorted(line.upper()))
    
    def remove_first_ele(self):
        for word in self.words:
            word.pop(0)

    def print_matching_words(self):
        for index in self.matches_index:
            print(self.original[index])

    #cycles through each word(sorted_list) in words
    #checks for a match against word and letter
        #if true, add index to index list
    def check_match(self, letters):
        index = 0
        copy_letters = letters.copy()
        for word in self.words:

            if self.has_match(word, copy_letters):
                self.matches_index.append(index)
                print(self.original[index])
                
            index+=1
    
    #if word length (word checking against) is == number of matches, there is a match
    #cycle through each letter in word, cycle through each letter in Letters (rack)
    #   if letter's match up, remove letter from Letters (rack)
    #this was my make or break function - I did not check it in isolation, rather booted the whole game to check
    # I could get a match for 'aa' 
    def has_match (self, word, letters):
        word_length = len(word)
        matches = 0
        copied_letters = letters.copy()
        for i in word:
            for letter in copied_letters:

                if(letter == i):
                    matches +=1
                    copied_letters.remove(letter)
                    
        if matches == word_length:
            return True

ben = Player()
game = Game(ben)
print(ben.print_letters())


# dict = Words()
# print(dict.words[6])




