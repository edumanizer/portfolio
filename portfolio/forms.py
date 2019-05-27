from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    username = forms.CharField(label = "Ваше имя:")
    email = forms.EmailField(label = "Ваш Email:")
    content = forms.CharField(widget = forms.Textarea, label = "Описание работы:")
    price = forms.FloatField(label = "Примерная стоимость:")
    phonenumber = forms.CharField(label = "Ваш номер телефона:")
    class Meta:
        model = Contact
        fields = ['username', 'email', 'content', 'phonenumber', 'price']