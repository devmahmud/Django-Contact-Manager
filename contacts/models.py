from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    GENDER_CHOICES = (
        ('male','Male'),
        ('female','Female')
    )
    manager = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_contacts')
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    info = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='images/%Y/%m/%d/',blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


