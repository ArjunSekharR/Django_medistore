from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    stocks = models.IntegerField()
    date_and_time = models.DateTimeField(auto_now_add=True)

