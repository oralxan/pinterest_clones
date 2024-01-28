from django.contrib.admin import register, ModelAdmin

from .models import Author

@register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = ('id', 'author')
    list_display_links = ('id', 'author')
    search_fields = ['author__istartswith','fating']
    ordering = ('author',)
