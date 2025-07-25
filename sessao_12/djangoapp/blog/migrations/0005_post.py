# Generated by Django 5.2.1 on 2025-07-17 20:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_page_content_page_is_published'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('slug', models.SlugField(blank=True, default='', max_length=100, null=True, unique=True)),
                ('is_published', models.BooleanField(default=False, help_text='Is this post published?')),
                ('excerpt', models.CharField(max_length=100)),
                ('content', models.TextField(default='')),
                ('cover', models.ImageField(blank=True, default='', upload_to='posts/%Y/%m/')),
                ('cover_in_post_content', models.BooleanField(default=False, help_text='Show cover in post content?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_created_by', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, default='', to='blog.tag')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
