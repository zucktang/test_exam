# Generated by Django 5.0.4 on 2024-08-11 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('acronym', models.CharField(max_length=10, unique=True)),
                ('address', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('K1', 'อนุบาล 1 (K1)'), ('K2', 'อนุบาล 2 (K2)'), ('K3', 'อนุบาล 3 (K3)'), ('G1', 'ประถมศึกษา 1 (G1)'), ('G2', 'ประถมศึกษา 2 (G2)'), ('G3', 'ประถมศึกษา 3 (G3)'), ('G4', 'ประถมศึกษา 4 (G4)'), ('G5', 'ประถมศึกษา 5 (G5)'), ('G6', 'ประถมศึกษา 6 (G6)'), ('G7', 'มัธยมศึกษา 1 (G7)'), ('G8', 'มัธยมศึกษา 2 (G8)'), ('G9', 'มัธยมศึกษา 3 (G9)'), ('G10', 'มัธยมศึกษา 4 (G10)'), ('G11', 'มัธยมศึกษา 5 (G11)'), ('G12', 'มัธยมศึกษา 6 (G12)')], max_length=10)),
                ('section', models.CharField(max_length=10)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='apis.school')),
            ],
            options={
                'abstract': False,
                'unique_together': {('school', 'grade', 'section')},
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'ผู้ชาย'), ('female', 'ผู้หญิง'), ('other', 'อื่นๆ')], max_length=10)),
            ],
            options={
                'abstract': False,
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'ผู้ชาย'), ('female', 'ผู้หญิง'), ('other', 'อื่นๆ')], max_length=10)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='apis.classroom')),
            ],
            options={
                'abstract': False,
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.CreateModel(
            name='TeacherClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='apis.classroom')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='apis.teacher')),
            ],
            options={
                'abstract': False,
                'unique_together': {('teacher', 'classroom')},
            },
        ),
    ]
