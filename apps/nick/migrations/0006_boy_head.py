# Generated by Django 2.1.2 on 2018-12-13 09:13

from django.db import migrations, models
import nick.models


class Migration(migrations.Migration):

    dependencies = [
        ('nick', '0005_discuss'),
    ]

    operations = [
        migrations.AddField(
            model_name='boy',
            name='head',
            field=models.ImageField(default='http://img3.duitang.com/uploads/item/201505/22/20150522205616_KeX3C.jpeg', upload_to=nick.models.image_upload_to),
        ),
    ]
