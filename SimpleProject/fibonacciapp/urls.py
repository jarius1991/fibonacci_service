from django.urls import path
from .views import generate_number

app_name = "fibonacci"

urlpatterns = [
    path('<int:index>', generate_number, name='index_value'),
]
