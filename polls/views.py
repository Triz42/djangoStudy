from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. YOU'RE AT THE POLLS INDEX!")
