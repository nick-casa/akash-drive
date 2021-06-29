# Generated by Django 3.2.4 on 2021-06-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('wallet', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
