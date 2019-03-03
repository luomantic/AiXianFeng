# Generated by Django 2.1.7 on 2019-03-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20190216_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='')),
                ('sex', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
    ]
