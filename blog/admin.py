from django.contrib import admin
from .models import Post
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "body", "approved", "created_on")
    list_filter = ("approved", "created_on", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# Register your models here.
admin.site.register(Comment, CommentAdmin)
