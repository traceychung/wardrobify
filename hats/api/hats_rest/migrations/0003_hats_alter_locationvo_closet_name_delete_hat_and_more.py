# Generated by Django 4.0.3 on 2022-12-03 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hats_rest', '0002_remove_hat_picture_url_hat_picture_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField(blank=True, null=True)),
                ('fabric', models.CharField(max_length=100)),
                ('style_name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='locationvo',
            name='closet_name',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Hat',
        ),
        migrations.AddField(
            model_name='hats',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hats', to='hats_rest.locationvo'),
        ),
    ]