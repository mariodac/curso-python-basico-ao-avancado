from django.contrib import admin
from blog.models import Tag
from blog.models import Category
from blog.models import Page

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)
    search_fields = ('id', 'name', 'slug',)
    list_per_page = 10
    ordering = ('-id',)
    prepopulated_fields = {
        "slug": ("name",),
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)
    search_fields = ('id', 'name', 'slug',)
    list_per_page = 10
    ordering = ('-id',)
    prepopulated_fields = {
        "slug": ("name",),
    }

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_published', )
    list_display_links = ('title',)
    search_fields = ('id', 'title', 'slug', 'content', )
    list_per_page = 10
    ordering = ('-id',)
    prepopulated_fields = {
        "slug": ("title",),
    }
    list_editable = ('is_published',)
    list_filter = ('is_published',)