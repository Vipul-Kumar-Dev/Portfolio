# Generated by Django 5.1.2 on 2025-06-19 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PF_App', '0003_remove_contactmessage_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FAQQuestion',
        ),
    ]
