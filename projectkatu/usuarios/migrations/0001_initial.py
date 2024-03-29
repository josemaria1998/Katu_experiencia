# Generated by Django 4.2.3 on 2023-07-25 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('idUsuario', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=300)),
                ('login', models.CharField(max_length=45)),
                ('senha', models.CharField(max_length=45)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=300, null=True)),
            ],
            options={
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('idCompra', models.BigAutoField(primary_key=True, serialize=False)),
                ('forma_pagamento', models.CharField(max_length=45)),
                ('data', models.DateField(auto_now_add=True, help_text='Formato <em> YYYT-MM-DD </em>')),
                ('fk_idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios')),
            ],
            options={
                'verbose_name_plural': 'Compra',
            },
        ),
    ]
