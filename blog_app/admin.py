from django.contrib import admin

from .models import Post, Category


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id',)


admin.site.register(Post)
admin.site.register(Category)

