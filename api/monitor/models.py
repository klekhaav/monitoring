from django.db import models


class Server(models.Model):
    user_email = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=150)
    port = models.IntegerField()

    def __str__(self):
        return self.title