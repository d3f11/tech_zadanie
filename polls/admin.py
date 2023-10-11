from django.contrib import admin
from .models import MainMenu, Menu


class MainMenuTabular(admin.TabularInline):
    model = MainMenu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [
        MainMenuTabular,
    ]

@admin.register(MainMenu)
class MainMenuAdmin(admin.ModelAdmin):
    pass