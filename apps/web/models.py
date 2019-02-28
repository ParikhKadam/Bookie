""" models """

from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Bookmarks(models.Model):
    """ Bookmarks """
    bm_id = models.CharField(max_length=7, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.TextField()
    image = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """ Make sure to generate a unique random bookmark id """
        if self.id is None:
            while True:
                random = get_random_string(7)
                if not Bookmarks.objects.filter(bm_id=random).exists():
                    self.bm_id = random
                    return super().save(*args, **kwargs)
                continue
        else:
            return super().save(*args, **kwargs)
