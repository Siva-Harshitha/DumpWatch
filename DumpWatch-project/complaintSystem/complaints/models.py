from django.db import models

# Create your models here.
class Complaint(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    complaint = models.TextField()
    marked = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='complaints/', blank=True, null=True)

    def _str_(self):
        return f"Complaint from {self.name}"