# Generated by Django 4.0.4 on 2022-04-24 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_id', models.IntegerField()),
                ('detail', models.TextField()),
                ('career', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Femail')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Candidate.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255)),
                ('level', models.CharField(choices=[('B', 'Basic'), ('I', 'Intermediate'), ('P', 'Professional')], max_length=1)),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Candidate.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('level', models.CharField(choices=[('B', 'Basic'), ('I', 'Intermediate'), ('P', 'Professional')], max_length=1)),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Candidate.candidate')),
            ],
        ),
    ]
