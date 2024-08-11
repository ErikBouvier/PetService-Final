# Generated by Django 3.2 on 2024-08-10 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PetService', '0003_auto_20240810_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='profesional_a_cargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PetService.veterinario'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='propietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PetService.propietario'),
        ),
    ]
