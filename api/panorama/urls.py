from django.urls import path
from api.panorama import views

urlpatterns = [
    path('en/api/get-panorama-images/', views.PanoramaImageListCreate.as_view()),
    path('en/api/get-panorama-image-models/', views.PanoramaImageModelListCreate.as_view()),
    path('en/api/get-panorama-image-links/', views.PanoramaImageLinkModelListCreate.as_view()),
]
