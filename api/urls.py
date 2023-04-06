from django.urls import path
from . import views
from .views import obtenerUno
urlpatterns = [
    path('get/',views.getTestimonios),
    path('post/',views.posTestimonios),
    path('get/<int:id>/',obtenerUno.as_view())
]
