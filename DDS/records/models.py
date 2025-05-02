from django.db import models
from guides.models import Category,Subcategory,Type,Status

# Create your models here.
class Record(models.Model):
   created_dt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
   status = models.ForeignKey(Status, on_delete=models.CASCADE,verbose_name='Статус',blank=True,null=True)
   type=models.ForeignKey(Type, on_delete=models.CASCADE,verbose_name='Тип',blank=False)
   category=models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Категория',blank=False)
   subcategory= models.ForeignKey(Subcategory, blank=False, on_delete=models.CASCADE,verbose_name='Подкатегория')
   summa=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Сумма',blank=False)
   Comment=models.TextField(max_length=200, null=True, blank=True,verbose_name='Комментарий')



