# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def main_page_en(request):
    return render(request, 'portfolio/main_page_en.html')

def main_page_rus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Спасибо за обращение, {username}! Я свяжусь с Вами в ближайшее время')
            return redirect('main-page-rus')
    else:
        form = ContactForm()
    template_name = 'portfolio/main_page_rus.html'
    context = {'form': form}
    return render(request, template_name, context)

def my_works(request):
    return render(request, 'portfolio/works.html')

