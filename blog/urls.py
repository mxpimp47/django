from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail, object_list

from testproject.blog.models import Entry
from tagging.views import tagged_object_list

info_dict = {'queryset': Entry.objects.all() }

urlpatterns = patterns('',
                       url(r'^(?P<object_id>\d]+)/$', object_detail, info_dict),
                       url(r'^$', object_list, info_dict),
                       )
