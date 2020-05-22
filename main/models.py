from django.db import models
from datetime import datetime

class blogCategory(models.Model):
    blog_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.blog_category

class blogSeries(models.Model):
    blog_series = models.CharField(max_length=200)
    blog_category = models.ForeignKey(blogCategory, default=1, verbose_name = "Category", on_delete = models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.blog_series

class blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_contents = models.TextField()
    blog_publishedDate = models.DateTimeField("Date Published",default=datetime.now())

    blog_series = models.ForeignKey(blogSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    blog_slug = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.blog_title
