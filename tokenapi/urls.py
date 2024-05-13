from django.urls import path
from .views import CustomAuthToken

app_name='tokenapi'

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
]
