from django.shortcuts import render
from django.http import HttpResponse
from . import game_logic as gl


testGame = gl.Game()

# test data
testPlayers = ['Harry','Hermione','Ron']
for player in testPlayers:
    testGame.players.append(gl.Player(player))

testGame.setup_game()

# Create your views here.
def gameSession(request):

    if request.method == 'POST':
        # Check if a "play_tile_action" button was clicked
        if 'play_tile_action' in request.POST:
            playerSeat = int(request.POST.get('player_seat'))
            playerUsername = request.POST.get('player_username')
            tileName = request.POST.get('play_tile_action')

            testGame.play_tile(playerSeat, playerUsername, tileName)
        elif 'end_turn_action' in request.POST:
            playerSeat = int(request.POST.get('player_seat'))
            playerUsername = request.POST.get('player_username')
            endTurn = request.POST.get('end_turn_action')

            testGame.end_turn(playerSeat)

    return render(request, 'game_board.html', {'testGame': testGame})