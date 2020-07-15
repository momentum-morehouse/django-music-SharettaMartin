from django.shortcuts import render
from .models import Album, Users
# Create your views here.


def index(request):
  mymusic = Album.objects.all()
  return render (request, "mytunes/list_albums.html", context={"mytunes": mymusic})







