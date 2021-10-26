# Generated by Django 3.2.6 on 2021-10-23 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0004_alter_a8sam1_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a8sam1',
            name='title',
            field=models.CharField(choices=[('شاليهات', 'شاليهات'), ('مخيمات', 'مخيمات'), ('قوارب صيد', 'قوارب صيد'), ('قوارب نزهه', 'قوارب نزهه'), ('غوص', 'غوص'), ('العاب مائية', 'العاب مائية'), ('مخيمات شاطئية', 'مخيمات شاطئية'), ('دراجات', 'دراجات')], max_length=15),
        ),
        migrations.AlterField(
            model_name='add_detail',
            name='cate',
            field=models.CharField(choices=[('شاليهات', 'شاليهات'), ('مخيمات', 'مخيمات'), ('قوارب صيد', 'قوارب صيد'), ('قوارب نزهه', 'قوارب نزهه'), ('غوص', 'غوص'), ('العاب مائية', 'العاب مائية'), ('مخيمات شاطئية', 'مخيمات شاطئية'), ('دراجات', 'دراجات')], max_length=15),
        ),
    ]