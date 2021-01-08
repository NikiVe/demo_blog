from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from authentication.models import Profile, CustomProfile

UserModel = get_user_model()



# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user')
#     list_filter = ('id', 'user')
#     verbose_name_plural = 'Profile'
#
#
# admin.site.register(Profile, ProfileAdmin)
# admin.site.register(CustomProfile)


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profile'


class UserAdmin(BaseUserAdmin):
    inlines = (
        ProfileInlineAdmin,
    )


admin.site.unregister(UserModel)
admin.site.register(UserModel, UserAdmin)

