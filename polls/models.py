from django.db import models
from django.utils import timezone


class Menu(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class MainMenu(models.Model):
    title = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    main_menu = models.ForeignKey('self', on_delete=models.CASCADE,
                                  blank=True, null=True,
                                  related_name='sub_mainmenu')
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField(default=timezone.now,
                                    verbose_name='дата публикации')

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return f'{self.menu} - {self.title}'
