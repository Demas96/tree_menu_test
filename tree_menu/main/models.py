from django.db import models


class Menu(models.Model):
    name = models.CharField('Name', max_length=255)
    parent = models.ForeignKey('self', on_delete=models.SET_DEFAULT, null=True, blank=True, default=None)
    serial_number = models.IntegerField('Serial number',  null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.name}'
