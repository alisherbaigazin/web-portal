import json

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from .models import Hello, Speciality, SpecialityList, PanoramaImage


@plugin_pool.register_plugin
class HelloPlugin(CMSPluginBase):
    model = Hello
    name = _("Hello Plugin")
    render_template = "hello_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class SpecialityItemPlugin(CMSPluginBase):
    model = Speciality
    name = _("Speciality Item Plugin")
    render_template = "speciality_item_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class SpecialityListPlugin(CMSPluginBase):
    model = SpecialityList
    name = _("Speciality List Plugin")
    render_template = "speciality_list_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class PanoramaPlugin(CMSPluginBase):
    model = PanoramaImage
    name = _("Panorama Image Plugin")
    render_template = "panorama_image.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
