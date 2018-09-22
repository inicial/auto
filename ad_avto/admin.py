from django.contrib import admin

from .models import Ad

# admin.site.register(Ad)


# регистрируем модель в админке
@admin.register(Ad)
class AdminAd(admin.ModelAdmin):
    """
    отображение в админке
    """
    # какие поля показывать
    list_display = ["id", "status", "title", "cost", "year"]
    # отсортировать по ID
    ordering = ["id"]
    list_display_links = ('title',)
    # list_editable = ["title"]
    search_fields = ["title", "cost"]
