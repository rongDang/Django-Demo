# Generated by Django 2.1.2 on 2018-12-06 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nick', '0003_auto_20181121_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', mdeditor.fields.MDTextField()),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('author_form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_form', to=settings.AUTH_USER_MODEL)),
                ('author_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_fo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', mdeditor.fields.MDTextField()),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry', to='nick.Blog')),
            ],
        ),
        migrations.AddField(
            model_name='commentreply',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_reply', to='nick.Comments'),
        ),
    ]