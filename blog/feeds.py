# -- coding: UTF-8 -- 
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.conf import settings

from .models import Post


class AllPostsRssFeed(Feed):
    title = settings.MY_TITLE
    link = "/"
    description = settings.MY_TITLE + "最新文章"

    def items(self):
        return Post.objects.all().filter(status = 1)

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body


class AllPostsAtomFeed(AllPostsRssFeed):
    feed_type = Atom1Feed
    subtitle = AllPostsRssFeed.description
