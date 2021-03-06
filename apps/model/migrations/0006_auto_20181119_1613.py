# Generated by Django 2.1.2 on 2018-11-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0005_shop_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scoce',
            options={'verbose_name': '成绩', 'verbose_name_plural': '成绩'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': '博客', 'verbose_name_plural': '博客'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '学生', 'verbose_name_plural': '学生'},
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=15, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='price',
            field=models.IntegerField(verbose_name='价格'),
        ),
    ]
