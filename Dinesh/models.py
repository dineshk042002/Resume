from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    summary = models.TextField()
    skills = models.TextField()
    education = models.TextField()
    experience = models.TextField()

    def __str__(self):
        return self.name
