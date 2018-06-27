from django.shortcuts import render
from .models import Bookmark, PersonalBookmark

# Create your views here.


def index(request):
    context = {'public_bookmarks': Bookmark.objects.all()}
    if request.user.is_anonymous:
        context['private_bokomarks'] = PersonalBookmark.objects.none()
    else:
        context['private_bookmarks'] = PersonalBookmark.objects.filter(
            user=request.user)
    return render(request, 'bookmarks/index.html', context)
