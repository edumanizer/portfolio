from django.contrib import admin
from django.urls import path, include
from portfolio import views as portfolio_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]
