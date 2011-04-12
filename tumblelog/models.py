from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.syndication.feeds import Feed
from django.db import models
# from django.db.models.signals import post_save

# from blog.models import Entry
# from links.models import Link


class TumbleItem(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    pub_date = models.DateTimeField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.content_type.name


# post_save.connect(create_tweet_item, sender=Entry)
# post_save.connect(create_tweet_item, sender=Link)


class LatestItems(Feed):
    title = "My Tumblelog: Links"
    link = "/tumblelog/"
    description = "Latest Items posted to mysite.com"
    description_template = 'feeds/description.html'

    def items(self):
        return TumbleItem.objects.all.order_by('-pub_date')[:10]
