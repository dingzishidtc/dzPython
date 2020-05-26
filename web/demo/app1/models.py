from django.db import models

# Create your models here.

class CreateUpdate(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class Person(CreateUpdate):
    # first_mame，last_name，crated_at,update_at
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
class Order(CreateUpdate):
    #order_id,order_desc,created_at,updated_at
    order_id = models.CharField(max_length=30,db_index=True) #db_index=True表示是外键，可与其他表关联
    order_desc = models.CharField(max_length=120)