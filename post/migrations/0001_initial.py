# Generated by Django 2.0.3 on 2018-04-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Başlık')),
                ('content', models.TextField(verbose_name='İcerik')),
                ('publising_Date', models.DateTimeField(auto_now=True, verbose_name='Yayınlanma Tarihi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['-publising_Date'],
            },
        ),
    ]
