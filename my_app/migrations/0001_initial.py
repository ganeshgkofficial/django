# Generated by Django 5.0.7 on 2024-08-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cost', models.IntegerField()),
                ('category', models.CharField(choices=[('veg', 'veg'), ('non', 'non veg')], max_length=20)),
            ],
        ),
    ]
