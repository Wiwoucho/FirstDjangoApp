from django.contrib import admin
from django.contrib.auth.models import Group, Permission, User

from ExamProject.main.models import AddBookingModel


class Properties_info(admin.ModelAdmin):
    list_display = ('name', 'price', 'locations', 'username')
    list_filter = ('price',)
    search_fields = ('name', 'locations')

    def username(self, obj):
        username = User.objects.get(pk=obj.user_id)
        return username


admin.site.register(AddBookingModel, Properties_info)



