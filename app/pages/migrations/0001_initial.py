# Generated by Django 2.2 on 2020-11-13 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('body', models.TextField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PageConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to='pages.Page')),
                ('origin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origins', to='pages.Page')),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connectors', to='pages.Page')),
            ],
        ),
    ]
