from django.contrib import admin

from .models import Category, Post, Tag, Img
from .forms import BlogPostForm

class PostAdmin(admin.ModelAdmin):
    form = BlogPostForm
    filter_horizontal = ('tags',)
    list_display = ('title', 'created_time', 'pub_date', 'modified_time', 'category', 'author',
                    'views', 'status'
                    )
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'genre', 'status', 'cover', 'creator')
class ImgAdmin(admin.ModelAdmin):
	list_display = ('name', 'head_pic', 'created')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Img, ImgAdmin)
