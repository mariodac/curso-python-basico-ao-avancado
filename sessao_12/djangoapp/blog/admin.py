from typing import Any
from django.contrib import admin
from blog.models import Post, Tag, Category, Page
from django_summernote.admin import SummernoteModelAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )
    list_display_links = ("name",)
    search_fields = (
        "id",
        "name",
        "slug",
    )
    list_per_page = 10
    ordering = ("-id",)
    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )
    list_display_links = ("name",)
    search_fields = (
        "id",
        "name",
        "slug",
    )
    list_per_page = 10
    ordering = ("-id",)
    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = (
        "id",
        "title",
        "slug",
        "is_published",
    )
    list_display_links = ("title",)
    search_fields = (
        "id",
        "title",
        "slug",
        "content",
    )
    list_per_page = 20
    ordering = ("-id",)
    prepopulated_fields = {
        "slug": ("title",),
    }
    list_editable = ("is_published",)
    list_filter = ("is_published",)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("id", "title", "is_published", "created_by")
    list_display_links = ("title",)
    search_fields = (
        "id",
        "title",
        "slug",
        "content",
        "excerpt",
    )
    list_per_page = 20
    ordering = ("-id",)
    readonly_fields = (
        "created_by",
        "created_at",
        "updated_at",
        "updated_by",
        "link",
    )
    prepopulated_fields = {
        "slug": ("title",),
    }
    list_editable = ("is_published",)
    list_filter = (
        "category",
        "tags",
        "is_published",
    )
    summernote_fields = ("content",)

    def link(self, obj):
        if not obj.pk:
            return '-'
        # url_post = reverse("blog:post", args=(obj.slug,))
        url_post = obj.get_absolute_url()
        safe_link = mark_safe(f'<a target="_blank" href="{url_post}">Ver post</a>')
        return safe_link
    

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        obj.save()
