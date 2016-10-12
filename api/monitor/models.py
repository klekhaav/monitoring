from django.db import models
from accounts.models import Customer


HTTP = 'http'
HTTPS = 'https'

protocol_choices = (
    (HTTP, 'Hyper Text Transfer Protocol'),
    (HTTPS, 'Hyper Text Transfer Protocol over SSL'),
)


# extended user manager
class Server(models.Model):
    user_email = models.OneToOneField(Customer)
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=150)
    protocol = models.CharField(max_length=100, choices=protocol_choices, default=HTTPS)

    def __str__(self):
        return self.title
