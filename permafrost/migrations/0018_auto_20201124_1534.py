# Generated by Django 3.1.3 on 2020-11-24 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permafrost', '0017_delete_permafrostcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='permafrostrole',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='permafrostrole',
            name='category',
            field=models.CharField(choices=[('administration', 'Administration'), ('staff', 'Staff'), ('user', 'User')], max_length=32, verbose_name='Role Type'),
        ),
    ]