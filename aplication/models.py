from django.db import models
from django.contrib.auth.models import User


class Imagem(models.Model):
    img = models.ImageField(upload_to='img')

    class Meta():
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __str__(self) -> str:

        return self.img.url


class Cidade(models.Model):
    nome = models.CharField(max_length=30)

    class Meta():
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self) -> str:
        return self.nome


class DiasVisita(models.Model):
    dia = models.CharField(max_length=20)

    class Meta():
        verbose_name = 'Dias de visita'
        verbose_name_plural = 'Dias de visitas'

    def __str__(self) -> str:
        return self.dia


class Horario(models.Model):
    horario = models.TimeField()

    class Meta():
        verbose_name = 'Horário'
        verbose_name_plural = 'Horários'

    def __str__(self) -> str:
        return str(self.horario)


class Imovel(models.Model):
    choices = (('V', 'Venda'),
               ('A', 'Aluguel'))
    choices_imovel = (('A', 'Apartamento'),
                      ('C', 'Casa'))
    imagens = models.ManyToManyField(Imagem)
    valor = models.FloatField()
    quartos = models.IntegerField()
    tamanho = models.FloatField()
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)
    rua = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=choices)
    tipo_imovel = models.CharField(max_length=1, choices=choices_imovel)
    numero = models.IntegerField()
    descricao = models.TextField()
    dias_visita = models.ManyToManyField(DiasVisita)
    horarios = models.ManyToManyField(Horario)

    class Meta():
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'

    def __str__(self) -> str:
        return self.rua


class Visitas(models.Model):
    choices = (('S', 'Segunda'),
               ('T', 'Terça'),
               ('Q', 'Quarta'),
               ('QI', 'Quinta'),
               ('SE', 'Sexta'),
               ('SA', 'Sabado'),
               ('D', 'Domingo'))
    choices_status = (('A', 'Agendado'),
                      ('F', 'Finalizado'),
                      ('C', 'Cancelado'))
    imovel = models.ForeignKey(Imovel, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dia = models.CharField(max_length=20)
    horario = models.TimeField()
    status = models.CharField(
        max_length=1, choices=choices_status, default="A")

    class Meta():
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'

    def __str__(self) -> str:
        return self.usuario.username
