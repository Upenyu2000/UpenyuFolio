# Generated by Django 4.1 on 2024-07-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_stack'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stack',
            old_name='stack',
            new_name='framework',
        ),
        migrations.AddField(
            model_name='stack',
            name='language',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
