from django.urls import path
from . import views

urlpatterns = [
    path('token/', views.token_view),
    path('token/refresh/', views.token_refresh_view)
]
