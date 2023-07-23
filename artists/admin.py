from django.contrib import admin
from .models import Artist, Work, CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username',)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    list_filter = ('user',)
    search_fields = ('name', 'user__username')


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'work_type')
    list_filter = ('work_type',)
    search_fields = ('link', 'work_type')
