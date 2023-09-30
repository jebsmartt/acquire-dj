# Created to house logic for the game
import random

class Tile:
    # Represents a tile that a player can play
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.name = f'{row}{column}'

class TileBag:
    # Represents the storage for game tiles not in play
    rows = ['A','B','C','D','E','F','G','H','I']
    columns = [1,2,3,4,5,6,7,8,9,10,11,12]

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
        self.occupancy = "empty"

class Grid:
    # Represents the gameboard grid of spaces on which the player plays
    rows = ['A','B','C','D','E','F','G','H','I']
    columns = [1,2,3,4,5,6,7,8,9,10,11,12]

    def __init__(self):
        self.spaces = []
        
        # fill the grid with spaces
        for r in Grid.rows:
            for c in Grid.columns:
                space = Space(r,c)
                self.spaces.append(space)

class Player:
    seats = [0,1,2,3,4,5]

    def __init__(self , username):
        self.seat = Player.seats.pop(0)
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
        activePlayers = 0
        for player in self.players:
            activePlayers += 1
            while len(player.tile_tray) < 6:
                player.draw_tile(self.tileBag)

        self.activePlayerIndex = random.randint(0,activePlayers-1)

    def play_tile(self, playerSeat, playerUsername, tileName):
        filtered_tile_tray = []

        for player in self.players:
            if playerSeat == str(player.seat):
                for tile in player.tile_tray:
                    if tile.name != tileName:
                        filtered_tile_tray.append(tile)
                player.tile_tray = filtered_tile_tray
                
        for space in self.grid.spaces:
            if tileName == space.name:
                space.occupancy = "indep"
        
    
    def end_turn(self):
        self.activePlayerIndex = (self.activePlayerIndex + 1) % len(self.players)
