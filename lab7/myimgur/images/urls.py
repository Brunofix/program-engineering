from django.urls import path
from .views import image_list
from .views import image_detail
from .views import create_image
from .views import create_comment

app_name = "images"	
urlpatterns = [
    path('', image_list, name="list"),
    path('<int:image_id>/', image_detail, name='detail'),
    path('new/', create_image, name='create'),
    path('<int:image_id>/comments/new/', create_comment, name='create_comment')
]