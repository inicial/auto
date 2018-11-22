from django.contrib import admin

from .models import Ad, Comments

# admin.site.register(Ad)


# регистрируем модель в админке
@admin.register(Ad)
class AdminAd(admin.ModelAdmin):
    """
    отображение в админке
    """
    # какие поля показывать
    list_display = ["id", "title", "cost", "year", "date", "status"]
    # отсортировать по ID
    ordering = ["id"]
    list_display_links = ('title',)
    # list_editable = ["title"]
    search_fields = ["title", "cost"]


@admin.register(Comments)
class AdminComments(admin.ModelAdmin):
    """
    отображение в админке
    """
    # какие поля показывать
    list_display = ["id", "name", "date", "status"]
    # отсортировать по ID
    ordering = ["id"]
    list_display_links = ('name',)
    # list_editable = ["title"]
    search_fields = ["text", "name", "desc"]
