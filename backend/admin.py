from django.contrib import admin
from backend.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
class UserModelAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["user_id", "email", "Firstname","Lastname" ,"is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ('User Credentials',{'fields': ['email', 'password']}),
        ('Personal info', {'fields': ('Firstname','Lastname')}),
        ('Permissions', {'fields': ['is_admin']}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "fields": ["email", "Firstname","Lastname","password1"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email","user_id"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User ,UserModelAdmin)
