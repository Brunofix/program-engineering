from django.urls import path
from .views import image_list
from .views import image_detail

urlpatterns=[
    path('', image_list, name="image_list"),
    path('<int:image_id>/', image_detail, name='image_detail')
]