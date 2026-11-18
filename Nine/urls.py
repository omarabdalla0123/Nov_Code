from django.urls import path
from . import views
urlpatterns = [
    path('nine/', views.hi_func)
]