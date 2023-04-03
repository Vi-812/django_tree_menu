from django.db import models


def get_level(self):
    if self.parent:
        return self.parent.level + 1
    else:
        return 1


class TreeMenu(models.Model):
    name = models.CharField('Наименование', max_length=50)
    uri = models.CharField('URL', max_length=255, blank=True, null=True)
    parent = models.ForeignKey(to='self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)
    left = models.IntegerField(blank=True, null=True)
    right = models.IntegerField(blank=True, null=True)
    level = models.IntegerField('Уровень меню', blank=True, null=True, default=get_level(parent))
    position = models.IntegerField('Позиция', blank=True, null=True)

    def __str__(self):
        level = self.level if self.level else 1
        i = u'| ' if level > 1 else ''
        return (u'|--' * (level - 1)) + i + self.name


    class Meta:
        db_table = 'category'
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ('left',)

    def save(self, *args, **kwargs):
        super(TreeMenu, self).save(*args, **kwargs)
        self.set_mptt()

    def set_mptt(self, left=1, parent=None, level=1):
        for i in type(self).objects.filter(parent=parent).order_by('position'):
            obj, children_count = i, 0
            while obj.children.exists():
                for child in obj.children.all():
                    children_count += 1
                    obj = child
            data = {
                'level': level,
                'left': left,
                'right': left + (children_count * 2) + 1
            }
            type(self).objects.filter(id=i.id).update(**data)
            left = data['right'] + 1
            self.set_mptt(left=data['left'] + 1, parent=i.id, level=data['level'] + 1)
