from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    category = models.CharField(max_length=200)
    URL = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalBookmark(Bookmark):
    user = models.ForeignKey(User, on_delete=models.CASCADE)