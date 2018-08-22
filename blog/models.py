from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    seo_title = models.CharField(max_length=60, null=True, blank=True)
    seo_description = models.CharField(max_length=165, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post(models.Model):
    STATUS_CHOICES = (
        ('Published', 'Published'),
        ('Draft', 'Draft'),
    )
    title = models.CharField(max_length=250)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seo_title = models.CharField(max_length=60, null=True, blank=True)
    seo_description = models.CharField(max_length=165, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.CharField(max_length=10, default='Draft', choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

