from django.contrib.admin import *
from .models import Post
@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('id','name','date')
    list_display_links =('id','name','date')
    search_fields = ['name']