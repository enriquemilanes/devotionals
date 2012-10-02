# -*- coding: utf-8 -*-

from django.db import models

class Devotional(models.Model):
    """Class to store daily devotionals
    
    """
    
    title = models.CharField(max_length=250)
    month = models.IntegerField()
    day = models.IntegerField()
    body = models.TextField()
    
    def __unicode__(self):
        return self.title 
    
    def get_words_count(self):
        return len(self.body.split(' ')) - 1