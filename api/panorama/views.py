from web_portal.models import PanoramaImageLinkModel, \
    PanoramaImageModel, PanoramaImage
from rest_framework import generics
from api.panorama.serializers import PanoramaImageSerializer, PanoramaSerializer, PanoramaImageLinkSerializer


class PanoramaImageListCreate(generics.ListCreateAPIView):
    serializer_class = PanoramaSerializer

    def get_queryset(self):
        if 'pk' in self.kwargs:
            queryset = PanoramaImage.objects.filter(pk=self.kwargs['pk'])
        else:
            queryset = PanoramaImage.objects.all()
        return queryset


class PanoramaImageModelListCreate(generics.ListCreateAPIView):
    serializer_class = PanoramaImageSerializer

    def get_queryset(self):
        if 'pk' in self.kwargs:
            queryset = PanoramaImageModel.objects.filter(pk=self.kwargs['pk'])
        else:
            queryset = PanoramaImageModel.objects.all()
        return queryset


class PanoramaImageLinkModelListCreate(generics.ListCreateAPIView):
    serializer_class = PanoramaImageLinkSerializer

    def get_queryset(self):
        if 'pk' in self.kwargs:
            queryset = PanoramaImageLinkModel.objects.filter(pk=self.kwargs['pk'])
        else:
            queryset = PanoramaImageLinkModel.objects.all()

        return queryset
