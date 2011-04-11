from django.db import models
from django.contrib.contenttypes import generic
from django.db.models import signals
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save

from blog.models import Entry
from links.models import Link


class TumbleItem(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    pub_date = models.DateTimeField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.content_type.name

	for modelname in [Entry, Link]:
		dispatcher.connect(create_tumble_item, signal=signals.post_save, sender=modelname)
		from django.contrib.syndication.feeds import Feed
		class LatestItems(Feed):
		    title = "My Tumblelog: Links"
		    link = "/tumblelog/"
		    description = "Latest Items posted to mysite.com"
		    description_template = 'feeds/description.html'

		    def items(self):
		        return TumbleItems.objects.all.order_by('-pub_date')[:10]
