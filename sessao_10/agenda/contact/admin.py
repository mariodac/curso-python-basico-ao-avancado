from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone",
        "email",
        "created_date",
        "show",
    )
    ordering = ("-first_name",)
    list_filter = ("created_date", "category")
    search_fields = (
        "first_name",
        "last_name",
        "phone",
    )
    list_per_page = 10
    list_max_show_all = 100
    list_editable = (
        "first_name",
        "last_name",
        "email",
        "show",
    )
    list_display_links = ("id", "phone")


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    ordering = (
        "id",
        "name",
    )
