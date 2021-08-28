# Generated by Django 3.2.6 on 2021-08-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('complete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]