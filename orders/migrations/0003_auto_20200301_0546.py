# Generated by Django 3.0.3 on 2020-03-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200225_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subs',
            name='cheese',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='subs',
            name='mushroom',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='subs',
            name='onion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='subs',
            name='pepper',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='ShoppingCart',
        ),
    ]
