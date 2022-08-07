# Generated by Django 3.2.7 on 2022-04-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_alter_updateform_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateform',
            name='specialist',
            field=models.CharField(choices=[('Physiatrist', 'Physiatrist'), ('Dermatologist', 'Dermatologist'), ('Pediatrician', 'Pediatrician'), ('Cardiologist', 'Cardiologist'), ('Nephrologist', 'Nephrologist'), ('Gynecologist', 'Gynecologist'), ('Pathologist', 'Pathologist'), ('Podiatrist', 'Podiatrist'), ('Family Physician', 'Family Physician'), ('Other', 'Other')], max_length=200),
        ),
    ]
