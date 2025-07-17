from django.contrib import admin
from blog.models import Post, Tag, Category, Page

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
    list_per_page = 20
    ordering = ('-id',)
    prepopulated_fields = {
        "slug": ("title",),
    }
    list_editable = ('is_published',)
    list_filter = ('is_published',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'created_by' )
    list_display_links = ('title',)
    search_fields = ('id', 'title', 'slug', 'content', 'excerpt', )
    list_per_page = 20
    ordering = ('-id',)
    readonly_fields = ('created_by', 'created_at', 'updated_at', 'updated_by', ) 
    prepopulated_fields = {
        "slug": ("title",),
    }
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published',)