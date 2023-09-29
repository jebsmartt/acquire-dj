# Created to house logic for the game

class Tile:
    # Represents a tile that a player can play
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.name = f'{row}{column}'

class TileBag:
    # Represents the storage for game tiles not in play
    rows = ['A','B','C','D','E','F','G','H','I']
    columns = [1,2,3,4,5,6,7,8,9,10]

    def __init__(self):
        self.contents = []

        # fill the bag
        for r in TileBag.rows:
            for c in TileBag.columns:
                new_tile = Tile(r,c)
                self.contents.append(new_tile)
        

class Space:
    # Represents spaces on the game board
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.name = f'{row}{column}'

class Grid:
    # Represents the gameboard grid of spaces on which the player plays
    rows = ['A','B','C','D','E','F','G','H','I']
    columns = [1,2,3,4,5,6,7,8,9,10]

    def __init__(self):
        self.spaces = []
        
        # fill the grid with spaces
        for r in Grid.rows:
            for c in Grid.columns:
                space = Space(r,c)
                self.spaces.append(space)

class Player:
    
    def __init__(self , username):
        self.username = username
        self.tile_tray = []

    def draw_tile(self,tileBag):
        self.tile_tray.append(tileBag.contents.pop(0))


class Game:

    def __init__(self):
        self.tileBag = TileBag()
        self.grid = Grid()
        self.players = []
        self.activePlayerIndex = None

    def setup_game(self):
        for player in self.players:
            while len(player.tile_tray) < 6:
                player.draw_tile(self.tileBag)

    
    def end_turn(self):
        self.activePlayerIndex = (self.activePlayerIndex + 1) % len(self.players)
