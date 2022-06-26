from django.contrib import admin
from zarafshon.models import Post, Tag, Messages
# Register your models here.

class CustomPostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

class CustomTagModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}    


class CustomMessageModelAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email', 'sender_message')
    


admin.site.register(Post, CustomPostModelAdmin)
admin.site.register(Tag, CustomTagModelAdmin)
admin.site.register(Messages, CustomMessageModelAdmin)