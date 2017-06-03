from django.contrib import admin

from . import models


class LoteInline(admin.StackedInline):
    model = models.Lote
    extra = 0


@admin.register(models.Leilao)
class LeilaoAdmin(admin.ModelAdmin):
    inlines = [
        LoteInline
    ]


class LanceInline(admin.StackedInline):
    model = models.Lance
    extra = 0


@admin.register(models.Lote)
class LoteAdmin(admin.ModelAdmin):
    inlines = [
        LanceInline,
    ]
