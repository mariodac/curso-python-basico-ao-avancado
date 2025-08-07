from django.db import models
from django.contrib.auth.models import User
from utils.rands import slugify_new
from utils.images import resize_image
from django_summernote.models import AbstractAttachment


class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
        current_file_name = str(self.file.name)
        super_save = super().save(*args, **kwargs)
        file_changed = False
        if self.file:
            file_changed = current_file_name != self.file.name
        if file_changed:
            resize_image(self.file, 900, True, 90)

        return super_save


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
    is_published = models.BooleanField(
        default=False, help_text="Is this page published?"
    )
    content = models.TextField(default="")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True).order_by("updated_at")

class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    objects = PostManager()

    title = models.CharField(max_length=70)
    slug = models.SlugField(
        unique=True, default="", null=True, blank=True, max_length=100
    )
    is_published = models.BooleanField(
        default=False, help_text="Is this post published?"
    )
    excerpt = models.CharField(max_length=100)
    content = models.TextField(default="")
    cover = models.ImageField(upload_to="posts/%Y/%m/", blank=True, default="")
    cover_in_post_content = models.BooleanField(
        default=False, help_text="Show cover in post content?"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add para adicionar a data na criação
    # user.post_created_by.all()
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="post_created_by",
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )  # auto_now para adicionar a data na atualização
    # # user.post_updated_by.all()
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="post_updated_by",
    )

    tags = models.ManyToManyField(Tag, blank=True, default="")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True, default=None
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)

        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False
        if self.cover:
            cover_changed = current_cover_name != self.cover.name
        if cover_changed:
            resize_image(self.cover, 900, True, 90)

        return super_save

    def __str__(self):
        return self.title
