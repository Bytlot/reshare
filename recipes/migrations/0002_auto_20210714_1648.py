# Generated by Django 3.2.5 on 2021-07-14 16:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ('title',), 'verbose_name': 'ingredient', 'verbose_name_plural': 'ingredients'},
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='dimension',
            field=models.CharField(max_length=64, verbose_name='Dimension'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='title',
            field=models.CharField(db_index=True, max_length=256, verbose_name='Ingredient name'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Recipe author'),
        ),
    ]
