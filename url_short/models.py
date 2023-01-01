from django.db import models


class Url(models.Model):
    full_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=16, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_url


class Clicks(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    date_clicked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
