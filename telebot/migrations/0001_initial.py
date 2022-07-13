# Generated by Django 4.0.5 on 2022-07-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeleSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_token', models.CharField(max_length=200, verbose_name='Токен')),
                ('tg_chat', models.CharField(max_length=200, verbose_name='Чат')),
                ('tg_massage', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Настройку',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
