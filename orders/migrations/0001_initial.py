# Generated by Django 3.0.3 on 2020-02-24 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(default='None', max_length=64)),
                ('size', models.CharField(default='Small', max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'parm',
            },
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(default='None', max_length=64)),
                ('size', models.CharField(default='Small', max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'pasta',
            },
        ),
        migrations.CreateModel(
            name='Platter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(default='regular', max_length=64)),
                ('parma', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='orders.Parm')),
            ],
            options={
                'db_table': 'platter',
            },
        ),
        migrations.CreateModel(
            name='RegularPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstTop', models.CharField(default='None', max_length=64)),
                ('secondTop', models.CharField(default='None', max_length=64)),
                ('thirdTop', models.CharField(default='None', max_length=64)),
                ('size', models.CharField(default='Small', max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'regularpizza',
            },
        ),
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(default='None', max_length=64)),
                ('size', models.CharField(default='Small', max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'salads',
            },
        ),
        migrations.CreateModel(
            name='SicilianPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstTop', models.CharField(default='None', max_length=64)),
                ('secondTop', models.CharField(default='None', max_length=64)),
                ('thirdTop', models.CharField(default='None', max_length=64)),
                ('size', models.CharField(default='Small', max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'sicilianpizza',
            },
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(default='None', max_length=64)),
                ('size', models.CharField(default='Small', max_length=64)),
                ('mushroom', models.IntegerField()),
                ('onion', models.IntegerField()),
                ('pepper', models.IntegerField()),
                ('cheese', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'sub',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greens', models.ManyToManyField(blank=True, related_name='greens', to='orders.Salads')),
                ('italy', models.ManyToManyField(blank=True, related_name='sicily', to='orders.SicilianPizza')),
                ('pastas', models.ManyToManyField(blank=True, related_name='linguini', to='orders.Pasta')),
                ('pizzas', models.ManyToManyField(blank=True, related_name='regulars', to='orders.RegularPizza')),
                ('platters', models.ManyToManyField(blank=True, related_name='plate', to='orders.Platter')),
                ('sandwich', models.ManyToManyField(blank=True, related_name='subway', to='orders.Subs')),
            ],
            options={
                'db_table': 'shoppingcart',
            },
        ),
        migrations.AddField(
            model_name='platter',
            name='salad',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='orders.Salads'),
        ),
        migrations.AddField(
            model_name='platter',
            name='ziti',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='orders.Pasta'),
        ),
    ]
