# Generated by Django 4.0.4 on 2022-05-13 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worksfor',
            name='chef',
        ),
        migrations.RemoveField(
            model_name='worksfor',
            name='shop',
        ),
        migrations.DeleteModel(
            name='ChefOrders',
        ),
        migrations.DeleteModel(
            name='WorksFor',
        ),
    ]
