# Generated by Django 3.0.4 on 2020-04-27 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baby', '0003_baby'),
        ('type', '0003_type'),
        ('event', '0002_delete_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('note', models.CharField(max_length=300)),
                ('baby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baby.Baby')),
                ('event_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='type.Type')),
            ],
        ),
    ]