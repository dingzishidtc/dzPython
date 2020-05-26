from django.contrib import admin
from app1.models import Person,Order

# Register your models here.

#注册模型
class PersonAdmin(admin.ModelAdmin):
    #该方法用于后台列表展示
    list_display = ("first_name","last_name","created_at")
    #增加右侧过滤器
    list_filter = ("first_name","last_name")
    #增加搜索功能
    search_fields = ("first_name","last_name")


admin.site.register(Person,PersonAdmin)