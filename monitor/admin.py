from django.contrib import admin

from .models import Camera  # 记得导包


@admin.register(Camera)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')  # 在后台列表下显示的字段
