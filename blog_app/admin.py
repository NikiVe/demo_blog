from django.contrib import admin

from .models import Post, Category, Comment


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id',)


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)

