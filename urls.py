from django.conf.urls.defaults import *

from django.contrib import admin

from tumblelog.models import LatestItems

feeds = {

    'tumblelog': LatestItems

}



# Uncomment the next two lines to enable the admin:

# from django.contrib import admin

admin.autodiscover()



urlpatterns = patterns('',

     (r'^admin/(.*)', admin.site.root),

	 (r'^blog/', include('testproject.blog.urls')),
	
	 (r'^tumblelog/', 'tumblelog.views.tumbler'), 
	 
	 (r'^tags/(?P<slug>[a-zA-Z0-9_.-]=)/$',
	'testproject.tag_views.tag_detail'),
	
	 (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

	
)



