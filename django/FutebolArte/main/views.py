from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"title": "Ta ok", "body": "<h1>Ta ok!</h1>"}
    return render(request, "main/main.html", context)
