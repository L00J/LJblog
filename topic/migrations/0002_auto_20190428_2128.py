# Generated by Django 2.1.5 on 2019-04-28 21:28

from django.db import migrations, models
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['ctime'], 'verbose_name': '专题文章', 'verbose_name_plural': '专题文章'},
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=mdeditor.fields.MDTextField(blank=True, null=True, verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='post',
            name='ctime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间'),
        ),
    ]
