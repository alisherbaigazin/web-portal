from rest_framework import serializers
from web_portal.models import PanoramaImageLinkModel, PanoramaImageModel, PanoramaImage


class PanoramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanoramaImage
        fields = ('id', 'name', 'images')


class PanoramaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanoramaImageModel
        fields = ('id', 'image', 'links')


class PanoramaImageLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanoramaImageLinkModel
        fields = ('id', 'image_link', 'image_link_name', 'x_axis', 'y_axis', 'z_axis')
