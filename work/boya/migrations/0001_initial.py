# Generated by Django 2.2.11 on 2020-03-13 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boyaci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
                ('telefon_no', models.CharField(max_length=11)),
                ('kayit_tarihi', models.DateTimeField(auto_now_add=True)),
                ('aciklama', models.TextField()),
            ],
        ),
    ]
