# Generated by Django 5.1.2 on 2025-06-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PF_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('question', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='best_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='preferred_contact',
            field=models.CharField(choices=[('email', 'Email'), ('phone', 'Phone')], default='email', max_length=10),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(default='General Inquiry', max_length=150),
            preserve_default=False,
        ),
    ]
