from django.contrib import admin

from .models import Post, Category, Comment


class CommentInline(admin.StackedInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'title', 'author', 'category', 'id')

    inlines = (CommentInline,)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)

