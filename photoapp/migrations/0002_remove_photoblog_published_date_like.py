# Generated by Django 4.2.2 on 2023-06-15 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoblog',
            name='published_date',
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photoblog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='photoapp.photoblog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
