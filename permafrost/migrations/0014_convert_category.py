# Generated by Django 3.0.7 on 2020-06-05 23:33

from django.db import migrations

def set_missing_category(apps, schema_editor):
    PermafrostRole = apps.get_model('permafrost', 'PermafrostRole')
    for role in PermafrostRole.objects.all():
        if not role.category and role.group:
            role.category = role.group.name.split("_")[1]
            role.save()


class Migration(migrations.Migration):

    dependencies = [
        ('permafrost', '0013_permafrostrole_category'),
    ]

    operations = [
        migrations.RunPython(set_missing_category, reverse_code=migrations.RunPython.noop),
    ]
