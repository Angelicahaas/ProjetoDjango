from django.db import models


class Reader(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    completed_name = models.CharField(max_length=50)
    email = models.CharFIeld(max_length=50)


    def __str__(self):
        return (f"{self.completed_name} {self.email}")