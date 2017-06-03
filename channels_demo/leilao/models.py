from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.db import models


class Leilao(models.Model):
    nome = models.CharField(
        verbose_name='Nome',
        max_length=30,
    )

    criado_em = models.DateTimeField(
        verbose_name='Data de Criação',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Leilão'
        verbose_name_plural = 'Leilões'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('leilao:leilao-detail', kwargs={'pk': self.pk})


class Lote(models.Model):
    leilao = models.ForeignKey(
        to='leilao',
    )

    descricao = models.TextField(
        verbose_name='Descrição',
    )

    criado_em = models.DateTimeField(
        verbose_name='Data de Criação',
        auto_now_add=True,
    )

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse_lazy('leilao:lote-detail', kwargs={'pk': self.pk})

    def get_ultimo_lance(self):
        return self.lance_set.latest()


class Lance(models.Model):
    lote = models.ForeignKey(
        to=Lote,
    )

    usuario = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
    )

    valor = models.DecimalField(
        verbose_name='Valor',
        max_digits=5,
        decimal_places=2,
    )

    criado_em = models.DateTimeField(
        verbose_name='Data de Criação',
        auto_now_add=True,
    )

    class Meta:
        get_latest_by = 'criado_em'
        ordering = (
            '-criado_em',
        )
