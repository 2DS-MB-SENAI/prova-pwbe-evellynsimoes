from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=30, null=True)
    especialidade = models.CharField(max_length=20, choices=[('Den', 'Dentista'),('Cir','Cirurgiao')]) 
    crm = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return f'{self.nome}, {self.especialidade}'

class Consulta(models.Model):
    paciente = models.CharField(max_length=20)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=[('agen', 'agendado'), ('rea', 'realizado'), ('cancel', 'cancelado')])

    def __str__(self):
        return f"A consulta é com o medico {self.medico}, na data {self.data}, com a paciente {self.paciente}, o status da consulta é {self.status}"
