from django.db import models


class Menu(models.Model):
    name = models.CharField('Name', max_length=255)
    parent = models.ForeignKey('self', on_delete=models.SET_DEFAULT, null=True, blank=True, default=None)
    serial_number = models.IntegerField('Serial number',  null=True, blank=True, default=None)
    level = models.IntegerField('Level',  null=True, blank=True, default=0)

    def __str__(self):
        if self.parent == None:
            self.level = 0
            print(self.level)
        else:
            self.level = self.parent.level + 1
            print(self.level)
        self.save()
        return f'{self.name}'
