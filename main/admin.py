from django.contrib import admin
from .models import blog, blogSeries, blogCategory
from  tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class blogAdmin(admin.ModelAdmin):
    fieldsets= [
        ("Title/date", {"fields" : ["blog_title","blog_publishedDate"]}),
        ("URL", {"fields":["blog_slug"]}),
        ("Series", {"fields":["blog_series"]}),
        ("Contents", {"fields":["blog_contents"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()}
    }

admin.site.register(blogSeries)
admin.site.register(blogCategory)
admin.site.register(blog, blogAdmin)
