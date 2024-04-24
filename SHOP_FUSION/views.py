from django.shortcuts import render

def about(request):
    return render(request, "about.html")


def team(request):
    return render(request, "team.html")