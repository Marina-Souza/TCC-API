from django.db import models

# Create your models here.


class Music(models.Model):
    
    class Meta:
        db_table = 'music'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()

    def __str__(self):
        return self.title

class Dispositivos(models.Model):
    
    class Meta:

        db_table = 'dispositivos'
    tipo = models.CharField(default='acionador', max_length=200)
    nome = models.CharField(max_length=200)
    GPIOPort = models.IntegerField()

    def __str__(self):
        return self.nome

class Coleta(models.Model):
    
    class Meta:
        db_table = 'coleta'

    idDispositivo = models.IntegerField()
    valor = models.IntegerField()
    data = models.DateField()

    def __str__(self):
        return self.idDispositivo

class Acionamentos(models.Model):
    
    class Meta:
        db_table = 'acionamentos'

    idDispositivo = models.ForeignKey(Dispositivos, on_delete=models.CASCADE)
    valor = models.IntegerField()
    modo = models.CharField(max_length=20, default='Manual')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.idDispositivo

class Alertas(models.Model):
    
    class Meta:
        db_table = 'alertas'

    idDispositivo = models.CharField(max_length=20, null=True) #models.ForeignKey(Dispositivos, on_delete=models.CASCADE)
    limiar = models.FloatField(null=True) 
    tipo = models.CharField(max_length=20, default='condutividade')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.limiar)

class Sistema(models.Model):
    
    class Meta:
        db_table = 'sistema'

    condutividade = models.FloatField(null=True) 
    vazao = models.IntegerField(null=True)
    cronIrrigacao = models.CharField(max_length=20, default='15 * * * *')
    umidade = models.IntegerField(null=True)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return str(self.condutividade)
