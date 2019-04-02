# Generated by Django 2.1.7 on 2019-04-02 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20190314_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50, unique=True)),
                ('order_createtime', models.DateTimeField(auto_now_add=True)),
                ('order_price', models.FloatField()),
                ('order_status', models.CharField(default=0, max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.User')),
            ],
            options={
                'db_table': 'axf_order',
            },
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=1)),
                ('price', models.FloatField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Goods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Order')),
            ],
            options={
                'db_table': 'axf_ordergoods',
            },
        ),
    ]