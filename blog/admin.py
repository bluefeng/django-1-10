from django.contrib import admin

from .models import Category, Post, Tag, Img
from .forms import BlogPostForm

class PostAdmin(admin.ModelAdmin):
    form = BlogPostForm
    filter_horizontal = ('tags',)
    list_filter = ('title',)
    exclude = ('author',)
    list_display = ('title', 'created_time', 'pub_date', 'modified_time', 'category', 'author',
                    'views', 'status'
                    )
    def save_model(self, request, obj, form, change):
    	if not change :
    		obj.author = request.user
    	super().save_model(request, obj, form, change)
class CategoryAdmin(admin.ModelAdmin):
	exclude = ('creator','resource')
	list_display = ('name', 'slug', 'genre', 'creator', 'status', 'cover')
	def save_model(self, request, obj, form, change):
		print(change)
		if not change :
			obj.creator = request.user
		super().save_model(request, obj, form, change)
class ImgAdmin(admin.ModelAdmin):
	list_display = ('name', 'head_pic', 'created')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Img, ImgAdmin)
