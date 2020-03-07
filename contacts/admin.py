from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

from .models import Contact

@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id','name','gender','email','info','phone')
    list_editable = ('info',)
    list_display_links = ('id','name')
    list_per_page = 10
    search_fields = ('name','gender','email','info','phone')
    list_filter = ('gender','date_added')
    date_hierarchy = ('date_added')


admin.site.unregister(Group)
