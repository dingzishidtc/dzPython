from django.contrib import admin
from app1.models import Person,Order

# Register your models here.

#ע��ģ��
class PersonAdmin(admin.ModelAdmin):
    #�÷������ں�̨�б�չʾ
    list_display = ("first_name","last_name","created_at")
    #�����Ҳ������
    list_filter = ("first_name","last_name")
    #������������
    search_fields = ("first_name","last_name")


admin.site.register(Person,PersonAdmin)