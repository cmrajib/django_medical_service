from django.contrib import admin


# Register your models here.
from UserRegistration.models import User



class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'healthcard', 'address_1', 'phone','city')
    list_display_links = ('email', 'full_name','healthcard')
    # list_filter = ('user__email','full_name','city')
    # list_editable = ('is_featured',)
    search_fields =('healthcard', 'full_name', 'phone')
    list_per_page = 10




admin.site.register(User, UserAdmin)
# admin.site.register(Profile, CarAdmin)


