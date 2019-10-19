# Generated by Django 2.2 on 2019-10-19 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll_ans', to='webapp.Poll', verbose_name='Опрос')),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='var_ans', to='webapp.Choice', verbose_name='Ответ')),
            ],
        ),
    ]
