from django.db import models

# Create your models here.


class Usuarios(models.Model):
    idUsuario = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length = 300,null=False)
    login = models.CharField(max_length = 45,null=False)
    senha = models.CharField(max_length = 45,null=False)
    cpf = models.CharField(max_length=11, null=False)
    telefone = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=300,null=True)


    class Meta:
        verbose_name_plural = "Usuários"


    def __str__(self):
        return self.cpf + " - " + self.nome



class Compra(models.Model):
    idCompra = models.BigAutoField(primary_key=True)
    forma_pagamento = models.CharField(max_length=45, null=False)
    data = models.DateField(auto_now_add=True, null=False,
                    help_text="Formato <em> YYYT-MM-DD </em>")
    fk_idUsuario = models.ForeignKey(Usuarios,on_delete= models.CASCADE)


    class Meta:
        verbose_name_plural = "Compra"


    def __str__(self):
        return self.data.strftime("%Y/%m/%d") +" - " + self.forma_pagamento