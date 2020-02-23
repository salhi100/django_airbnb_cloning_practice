# Generated by Django 3.0.3 on 2020-02-16 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0004_auto_20200216_0052'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
                ('rooms', models.ManyToManyField(blank=True, related_name='lists', to='rooms.Room')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='list', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]