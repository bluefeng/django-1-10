from django.contrib.sitemaps import GenericSitemap

from .models import Category, Post

post_info_dict = {
    'queryset': Post.objects.all().filter(status = 1),
    'date_field': 'modified_time',
}

sitemaps = {'post': GenericSitemap(post_info_dict, priority=0.6),}
