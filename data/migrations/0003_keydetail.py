# Generated by Django 2.1 on 2021-01-09 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20210106_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapillaryKey', models.CharField(blank=True, max_length=150, null=True)),
                ('GoogleLoginClientID', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]