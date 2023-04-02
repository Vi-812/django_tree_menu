from django.db import models
from mptt import register
from mptt.models import MPTTModel, TreeForeignKey


class Menu(MPTTModel):
    name = models.CharField('Наименование', max_length=50)
    uri = models.CharField('URL', max_length=255, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')

    class Meta:
        db_table = 'category'
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        # ordering = ('tree_id', 'level')

    def __str__(self):
        return str(self.name)


register(Menu, order_insertion_by=['name'])

# position = models.PositiveIntegerField('Позиция', default=1)
