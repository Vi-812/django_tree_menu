from django.db import models


class TreeMenu(models.Model):
    name = models.CharField('Наименование', max_length=50)
    uri = models.CharField('URL', max_length=255, blank=True, null=True)
    parent = models.ForeignKey(to='self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL, verbose_name='Родитель')
    position = models.FloatField('Позиция', blank=True, null=True)
    level = models.IntegerField(default=0)
    global_position = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ('global_position',)

    def __str__(self):
        return '|>>> ' * (self.level) + str(self.name)

    def save(self, *args, **kwargs):
        if self.parent:
            self.level = self.parent.level + 1
        if not self.position:
            self.position = 999
        super().save(*args, **kwargs)
        self.menu_sorting()

    def menu_sorting(self, level=0, parent=None, global_position=0):
        for pos, menu_item in enumerate(type(self).objects.filter(parent=parent).order_by('position')):
            global_position += 1 / (pow(10, level))
            data = {
                'position': pos + 1,
                'global_position': global_position,
            }
            type(self).objects.filter(id=menu_item.id).update(**data)
            if menu_item.children.exists():
                self.menu_sorting(level=level+1, parent=menu_item.id, global_position=global_position)



    # def set_mptt(self, left=1, parent=None, level=1):
    #     for i in type(self).objects.filter(parent=parent).order_by('position'):
    #         obj, children_count = i, 0
    #         while obj.
    #             for child in obj.children.all():
    #                 children_count += 1
    #                 obj = child
    #         data = {
    #             'level': level,
    #             'left': left,
    #             'right': left + (children_count * 2) + 1
    #         }
    #         type(self).objects.filter(id=i.id).update(**data)
    #         left = data['right'] + 1
    #         self.set_mptt(left=data['left'] + 1, parent=i.id, level=data['level'] + 1)
