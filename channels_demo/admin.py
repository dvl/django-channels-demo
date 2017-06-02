from django.contrib import admin

from . import models


class LanceInline(admin.StackedInline):
    model = models.Lance
    extra = 0


@admin.register(models.Lote)
class LoteAdmin(admin.ModelAdmin):
    inlines = (
        LanceInline,
    )
