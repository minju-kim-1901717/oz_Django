from django.contrib import admin

from todo.models import Todo


# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id','title','detail']
    list_display_links = ['title', 'detail']