from django.shortcuts import render
from django.http import HttpResponse
from . import game_logic as gl

# Create your views here.

# def index(request):
#     return HttpResponse("This is the HTTP Response for the Game app")

def index(request):
    # x = []
    # for i in range(10):
    #     x.append(i)

    # # Generate the HTML for the table
    # table_html = "<h1>Below this line there should be a table:</h1>"
    # table_html += "<table border='1'><tr><th>Index</th><th>Value</th></tr>"

    # for index, item in enumerate(x):
    #     table_html += f"<tr><td>{index}</td><td>{item}</td></tr>"

    # table_html += "</table>"

    # return HttpResponse(table_html)


    testGame = gl.Game()

    # test data
    testPlayers = ['Harry','Hermione','Ron']
    for player in testPlayers:
        testGame.players.append(gl.Player(player))

    testGame.setup_game()

    test_html = "<h1>Acquire! I hope...</h1>"

    # Generate the HTML table for each player's tray
    test_html += "<table border='1'>"
    for player in testGame.players:
        test_html += f"<tr><th>{player.username}</th></tr>"
        for tile in player.tile_tray:
            test_html += f"<tr><td>{tile.name}</td></tr>"
    test_html +="</table>"

    # Generate the HTML for the grid
    test_html += "<h2>Below this line there should the grid:</h2>"
    test_html += "<table border='1'>"
    for space in testGame.grid.spaces:
        test_html += f"<tr><td>{space.name}</td></tr>"
    test_html +="</table>"

    return HttpResponse(test_html)