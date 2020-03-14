# Generated by Django 2.2.11 on 2020-03-14 08:09

from django.db import migrations, models
import django.db.models.deletion


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
        migrations.CreateModel(
            name='Etiket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etiket_adi', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VerilenIs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_tarihi', models.DateTimeField(auto_now_add=True)),
                ('is_aciklama', models.TextField()),
                ('is_alan_boyaci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verilen_isler', to='boya.Boyaci')),
            ],
        ),
        migrations.AddField(
            model_name='boyaci',
            name='boyaci_etiket',
            field=models.ManyToManyField(related_name='boyacilar', to='boya.Etiket'),
        ),
    ]