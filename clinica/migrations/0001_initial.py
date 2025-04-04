# Generated by Django 4.2 on 2025-04-04 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, null=True)),
                ('especiaidade', models.CharField(choices=[('Den', 'Dentista'), ('Cir', 'Cirurgiao')], max_length=20)),
                ('crm', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.CharField(max_length=20)),
                ('data', models.DateTimeField()),
                ('status', models.CharField(choices=[('agen', 'agendado'), ('rea', 'realizado'), ('cancel', 'cancelado')], max_length=8)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.medico')),
            ],
        ),
    ]
