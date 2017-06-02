from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.db import models


class Lote(models.Model):
    nome = models.CharField(
        max_length=30
    )

    descricao = models.CharField(
        max_length=200
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('lotes-detail', kwargs={'pk': self.pk})

    def get_ultimo_lance(self):
        return self.lance_set.latest()


class Lance(models.Model):
    lote = models.ForeignKey(
        Lote
    )

    valor = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        get_latest_by = 'criado_em'
        ordering = ('-criado_em',)
