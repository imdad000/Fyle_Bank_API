# Generated by Django 2.2.3 on 2019-07-16 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fyleApp', '0003_branches_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('b_id', models.BigIntegerField(unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='branches',
            name='bank_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fyleApp.Bank'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='state',
            field=models.CharField(max_length=40),
        ),
    ]