# Generated by Django 5.0.6 on 2024-06-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode', '0008_alter_graph1_seat_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graph1',
            name='seat_type',
        ),
        migrations.AddField(
            model_name='graph1',
            name='seat',
            field=models.CharField(default='OPEN', max_length=200),
        ),
    ]