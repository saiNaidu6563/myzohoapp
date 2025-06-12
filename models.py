from django.db import models

class Lead(models.Model):
    lname = models.CharField(max_length=100)
    lemail = models.EmailField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lname