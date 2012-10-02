from devotionals.views import DevotionalTemplateView
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.detail import DetailView
from devotionals.models import Devotional

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'devotionals.views.home', name='home'),
    # url(r'^devotionals/', include('devotionals.foo.urls')),
    
    url(r'^home/(?P<date>\d+-\d+-\d+)/$', DevotionalTemplateView.as_view(), name='devotional_main_view'),
    url(r'^count/(?P<pk>\d+)/$', DetailView.as_view(template_name='count.html', model=Devotional), name='devotional_count_view'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


#MEDIA
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
