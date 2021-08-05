from django.db import models

# Create your models here.
class TicketBookModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, default=None)
    movie_name = models.CharField(max_length=30)
    ticket_no = models.IntegerField()
    no_of_tickets = models.IntegerField()