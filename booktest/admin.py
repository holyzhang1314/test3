from django.contrib import admin
from booktest.models import  AreaInfo
# Register your models here.

class AreaInfoAdmin(admin.ModelAdmin):

    list_per_page = 10
    list_display = ['id','atitle','title','parent']
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['atitle']
    search_fields = ['atitle']


admin.site.register(AreaInfo,AreaInfoAdmin)
