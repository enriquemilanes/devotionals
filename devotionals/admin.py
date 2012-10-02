# -*- coding: utf-8 -*-
from devotionals.models import Devotional
from django.contrib import admin


class DevotionalsOptions(admin.ModelAdmin):
    list_display = ("title",)
    
admin.site.register(Devotional, DevotionalsOptions)
 

