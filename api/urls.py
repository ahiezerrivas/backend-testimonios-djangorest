from django.urls import path
from . import views

urlpatterns = [
    path('get/',views.getTestimonios),
    path('post/',views.posTestimonios)
]
