# Generated by Django 4.0.3 on 2022-04-05 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('birth', models.DateField()),
                ('document', models.IntegerField(unique=True)),
            ],
        ),
    ]
