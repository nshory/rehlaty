# Generated by Django 3.2.6 on 2021-10-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0002_remove_add_detail_cate'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_detail',
            name='cate',
            field=models.CharField(choices=[('شاليهات', 'شاليهات'), ('مخيمات', 'مخيمات'), ('قوارب صيد', 'قوارب صيد'), ('قوارب نزهة', 'قوارب نزهة')], default='', max_length=15),
            preserve_default=False,
        ),
    ]