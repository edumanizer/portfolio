from django.urls import path
from .import views

urlpatterns = [
    path('', views.main_page_rus, name = 'main-page-rus'),
    path('en', views.main_page_en, name = 'main-page-en'),
    path('works', views.my_works, name = 'my-works'),
]
