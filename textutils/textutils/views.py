from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Prakash Shukla</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django CodeWithHary</a>>''')

def about(request):
    return HttpResponse("Prakash Shukla is ladchat")