# Generated by Django 2.1.7 on 2019-03-21 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('klass', '__first__'),
        ('departments', '__first__'),
        ('parents', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media')),
                ('roll', models.IntegerField()),
                ('registration', models.IntegerField()),
                ('phone', models.CharField(max_length=11, null=True)),
                ('session_start', models.DateField(verbose_name='Session start')),
                ('session_end', models.DateField(verbose_name='Session start')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Department')),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klass.Klass')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parents.Guardian')),
            ],
        ),
    ]
