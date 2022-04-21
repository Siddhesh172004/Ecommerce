# Generated by Django 4.0.2 on 2022-04-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_mens_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mens',
            name='category',
            field=models.CharField(choices=[('Mens', 'Mens'), ('Womens', 'Womens'), ('Kids', 'Kids'), ('Accessories', 'Accessories')], max_length=50),
        ),
        migrations.AlterField(
            model_name='mens',
            name='subcategory',
            field=models.CharField(choices=[('Casual', 'Casual'), ('Athletic', 'Athletic'), ('Sandals', 'Sandals'), ('Clog', 'Clog')], max_length=100),
        ),
    ]