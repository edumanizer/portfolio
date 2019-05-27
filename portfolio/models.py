from django.db import models
from django.forms import ModelForm


class Contact(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField()
    content = models.CharField(max_length=255)
    price = models.FloatField(blank=True)
    phonenumber = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.username

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['username', 'email', 'content', 'price', 'phonenumber'] 