from django.urls import path
from api.panorama import views

urlpatterns = [
    path('en/api/panorama-image/', views.PanoramaImageListCreate.as_view()),
    path('en/api/panorama-image-model/', views.PanoramaImageModelListCreate.as_view()),
    path('en/api/panorama-image-link/', views.PanoramaImageLinkModelListCreate.as_view()),
]
