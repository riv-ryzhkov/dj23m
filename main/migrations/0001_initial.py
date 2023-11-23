# Generated by Django 4.2.7 on 2023-11-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('text', models.TextField(verbose_name='Опис')),
                ('published', models.CharField(max_length=4, verbose_name='Рік видання')),
                ('count', models.IntegerField(default=1, verbose_name='Кількість')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]