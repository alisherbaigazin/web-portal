from django.contrib import admin

from web_portal.models import PanoramaImage, PanoramaImageModel, PanoramaImageLinkModel

admin.site.register(PanoramaImage)
admin.site.register(PanoramaImageModel)
admin.site.register(PanoramaImageLinkModel)