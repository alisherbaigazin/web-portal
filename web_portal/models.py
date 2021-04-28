from cms.models.pluginmodel import CMSPlugin

from django.db import models
from cms.models.pagemodel import Page


class Hello(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Guest')


class Speciality(CMSPlugin):
    name = models.CharField(max_length=50, default='name')
    short_description = models.CharField(max_length=100, default='short_description')
    description = models.CharField(max_length=200, default='description')
    footer = models.CharField(max_length=50, default='footer')
    image = models.ImageField()
    page_link = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='page_link', blank=True, null=True)

    def __str__(self):
        return self.name


class SpecialityList(CMSPlugin):
    list_title = models.CharField(max_length=50, default='list_title')
    short_description = models.CharField(max_length=100, default='short_description')
    description = models.CharField(max_length=200, default='description')
    related_link = models.ManyToManyField(blank=True, to='Speciality', verbose_name="Related List")

    def paired_list(self):
        paired_spec_list = []
        specs = self.related_link.all()
        sz = len(specs)
        print(sz)

        for i in range(0, sz, 2):
            if i+1 >= sz or sz < 2:
                paired_spec_list.append((specs[i], None))
            else:
                paired_spec_list.append((specs[i], specs[i+1]))

        return paired_spec_list

    def copy_relations(self, oldinstance):
        self.related_link.set(oldinstance.related_link.all())