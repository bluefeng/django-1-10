import os

from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Max, Sum
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

import markdown
from comments.models import BlogComment
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from model_utils import Choices
from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class Img(models.Model):
    name = models.CharField(_('图片名(描述)'), max_length = 100)
    head_pic = models.ImageField('图片',upload_to = 'blog/%Y/%m/%d/')
    created = models.DateTimeField(_('创建时间'), auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['-created']
        verbose_name = '图片'
        verbose_name_plural = '图片'

class Tag(models.Model):
    name = models.CharField(_('名字'), max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Category(models.Model):
    GENRE_CHOICES = Choices(
        (1, 'collection', _('普通')),
        (2, 'tutorial', _('教程')),
    )

    STATUS_CHOICES = Choices(
        (1, 'ongoing', _('进行中')),
        (2, 'finished', _('已完成')),
    )

    name = models.CharField(_('名字'), max_length=100)
    title = models.CharField(_('标题'), max_length=255, blank=True)
    slug = models.SlugField(_('英文名'), unique=True)
    description = models.TextField(_('描述'), blank=True)
    created = models.DateTimeField(_('creation time'), auto_now_add=True)
    genre = models.PositiveSmallIntegerField(_('类型'), choices=GENRE_CHOICES,
                                             default=GENRE_CHOICES.collection)
    status = models.PositiveSmallIntegerField(_('状态(教程使用)'), choices=STATUS_CHOICES,
                                              blank=True, null=True)
    cover = models.ImageField(_('封面(教程使用)'), upload_to='covers/categories/%Y/%m/%d/', blank=True)
    cover_thumbnail = ImageSpecField(source='cover',
                                     processors=[ResizeToFill(500, 300)],
                                     format='JPEG',
                                     options={'quality': 90})
    cover_caption = models.CharField(_('封面标题(教程使用)'), max_length=255, blank=True)
    resource = models.URLField(_('资源(废弃)'), blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('作者'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.name

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:category_slug', kwargs={'slug': self.slug})

    def total_views(self):
        if not self.post_set.exists():
            return {'category_views': 0}

        return self.post_set.aggregate(category_views=Sum('views'))

    def last_modified(self):
        return self.post_set.aggregate(last_modified=Max('modified_time'))
    class Meta:
        verbose_name = '类别'
        verbose_name_plural = '类别'


def post_cover_path(instance, filename):
    return os.path.join('posts', str(instance.pk), filename)


@python_2_unicode_compatible
class Post(models.Model):
    STATUS_CHOICES = Choices(
        (1, 'published', '发布'),
        (2, 'draft', '草稿'),
        (3, 'hidden', '隐藏'),
        (4, 'secret', '秘密'),
    )

    status = models.PositiveSmallIntegerField(_('状态'), choices=STATUS_CHOICES,
                                              default=STATUS_CHOICES.draft)
    title = models.CharField(_('标题'),max_length=255)
    body = models.TextField(_('内容'))
    excerpt = models.CharField(_('摘要'), max_length=255, blank=True)
    views = models.PositiveIntegerField(_('查看次数'), default=0, editable=False)
    pub_date = models.DateTimeField(_('发布时间'), blank=True, null=True)

    # Do not user auto_add=True or auto_now_add=True since value is None before instance be saved
    created_time = AutoCreatedField(_('创建时间'))
    modified_time = AutoLastModifiedField(_('修改时间'))
    cover = models.ImageField(_('封面'), upload_to=post_cover_path, blank=True)
    cover_thumbnail = ImageSpecField(source='cover',
                                     processors=[ResizeToFill(60, 60)],
                                     format='JPEG',
                                     options={'quality': 90})
    category = models.ForeignKey(Category, verbose_name=_('类别'), null=True, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name=_('标签'), blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('作者'))
    comments = GenericRelation(BlogComment, object_id_field='object_pk',
                               content_type_field='content_type')
    class Meta:
        ordering = ['-created_time']
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # TODO: refactor and test
            self.excerpt = strip_tags(md.convert(self.body))[:150]

        if not self.pub_date and self.status == self.STATUS_CHOICES.published:
            self.pub_date = self.created_time

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def word_count(self):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        # TODO: refactor and test
        return len(strip_tags(md.convert(self.body)))

    def is_tutorial(self):
        if not self.category:
            return False
        return self.category.get_genre_display() == 'tutorial'

    def root_comments(self):
        # TODO: move the logic to comment manager
        return self.comments.filter(parent__isnull=True, is_public=True, is_removed=False)

    def participants_count(self):
        return self.comments.values_list('user_id', flat=True).distinct().count()

