# Generated by Django 4.2.2 on 2023-10-08 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobno', models.CharField(default='', max_length=10)),
                ('city', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=50)),
                ('Photo', models.ImageField(default='', upload_to='static/invited')),
                ('partydate', models.CharField(default='', max_length=50)),
            ],
        ),
    ]