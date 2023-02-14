from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from users.models import User


class UserAdmin(BaseUserAdmin):
    pass
    # list_display = (
    #     'email', 'username', 'first_name', 'last_name', 'is_staff')
    # list_filter = ('is_staff', 'is_active', 'date_joined', 'last_login')
    # search_fields = ('email', 'username', 'first_name', 'last_name')
    # ordering = ('email',)
    # filter_horizontal = ()
    # fieldsets = (
    #     (None, {'fields': ('email', 'username', 'password')}),
    #     ('Personal info', {'fields': ('first_name', 'last_name')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
    #                                 'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'username', 'password1', 'password2'),
    #     }),
    # )


admin.site.register(User, UserAdmin)
