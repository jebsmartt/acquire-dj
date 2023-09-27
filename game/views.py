from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("This is the HTTP Response for the Game app")

def index(request):
    x = []
    for i in range(10):
        x.append(i)

    # Generate the HTML for the table
    table_html = "<h1>Below this line there should be a table:</h1>"
    table_html += "<table border='1'><tr><th>Index</th><th>Value</th></tr>"

    for index, item in enumerate(x):
        table_html += f"<tr><td>{index}</td><td>{item}</td></tr>"

    table_html += "</table>"

    return HttpResponse(table_html)