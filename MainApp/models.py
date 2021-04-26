from django.db import models
import datetime

LANG_CHOICE = [
    ('py', 'python'),
    ('cpp', 'C++'),
    ('js', 'javascript'),
]


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANG_CHOICE, default="py")
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(default=datetime.datetime.now)
