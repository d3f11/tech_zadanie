# Generated by Django 4.2.6 on 2023-10-11 08:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата публикации')),
                ('main_menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_mainmenu', to='polls.mainmenu')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.menu')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
