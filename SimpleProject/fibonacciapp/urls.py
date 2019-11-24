from django.urls import path
from .views import calculate_fibonacci_number

app_name = "fibonacci"

urlpatterns = [
    path('<int:index>', calculate_fibonacci_number, name='index_value'),
]
