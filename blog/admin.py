from django.contrib import admin
from .models import Post
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "body", "approved", "created_on")
    list_filter = ("approved", "created_on", "body")
    search_fields = ("author__username", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
