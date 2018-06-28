from django.shortcuts import render
from .models import Bookmark, PersonalBookmark
from .forms import BookmarkForm

# Create your views here.


def index(request):
    # import pdb
    # pdb.set_trace()
    pbid = PersonalBookmark.objects.values_list('id')
    context = {'form': BookmarkForm}
    context['public_bookmarks'] = Bookmark.objects.exclude(id__in=pbid)
    if request.user.is_anonymous:
        context['private_bookmarks'] = PersonalBookmark.objects.none()
    else:
        context['private_bookmarks'] = PersonalBookmark.objects.filter(
            user=request.user)
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        form.save()
        if form.is_valid():
            form.save()
        else:
            # TODO DISPLAY ERROR
            pass
    return render(request, 'bookmarks/index.html', context)
