# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from kioskapp.app.models import Competition, Club, Major, OurStory

# Register your models here.

admin.site.register(Competition)
admin.site.register(Club)
admin.site.register(Major)
admin.site.register(OurStory)
