from django.db import models
from utils.rands import slugify_new


class Tag(models.Model):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=100
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=100
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Page(models.Model):
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default="", null=True, blank=True, max_length=100
    )
    is_published = models.BooleanField(default=False, help_text="Is this page published?")
    content = models.TextField(default="")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title