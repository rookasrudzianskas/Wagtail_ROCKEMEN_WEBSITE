# Generated by Django 3.1.7 on 2021-04-14 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Enter your Facebook URL ')),
                ('twitter', models.URLField(blank=True, help_text='Enter your twitter URL ')),
                ('youtube', models.URLField(blank=True, help_text='Enter your YouTube URL ')),
                ('instagram', models.URLField(blank=True, help_text='Enter your instagram URL ')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
