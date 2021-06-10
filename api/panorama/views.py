from web_portal.models import PanoramaImageLinkModel, \
    PanoramaImageModel, PanoramaImage
from rest_framework import generics
from api.panorama.serializers import PanoramaImageSerializer, PanoramaSerializer, PanoramaImageLinkSerializer


class PanoramaImageListCreate(generics.ListCreateAPIView):
    queryset = PanoramaImage.objects.all()
    serializer_class = PanoramaSerializer


class PanoramaImageModelListCreate(generics.ListCreateAPIView):
    queryset = PanoramaImageModel.objects.all()
    serializer_class = PanoramaImageSerializer


class PanoramaImageLinkModelListCreate(generics.ListCreateAPIView):
    queryset = PanoramaImageLinkModel.objects.all()
    serializer_class = PanoramaImageLinkSerializer
