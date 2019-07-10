from django.contrib import admin
from .models import Paintings, Question, Comment

admin.site.register(Paintings)
admin.site.register(Question)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)
