# Generated by Django 5.0.3 on 2024-04-21 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ity', '0004_alter_mono_cloth_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mono',
            name='digital',
        ),
        migrations.RemoveField(
            model_name='mono',
            name='kind',
        ),
        migrations.RemoveField(
            model_name='mono',
            name='more_info',
        ),
        migrations.RemoveField(
            model_name='mono',
            name='types',
        ),
        migrations.AddField(
            model_name='mono',
            name='cloth_size',
            field=models.CharField(blank=True, choices=[('Xlarge', 'Xlarge'), ('large', 'large'), ('medium', 'medium'), ('slimfit', 'slimfit')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mono',
            name='COLOR',
            field=models.CharField(choices=[('green', 'green'), ('red', 'red'), ('black', 'black'), ('orange', 'orange'), ('purple', 'purple'), ('white', 'white'), ('gold', 'gold'), ('indigo', 'indigo'), ('brown', 'brown'), ('yellow', 'yellow'), ('grey', 'grey'), ('dark red', 'dark red'), ('turquoise', 'turquoise'), ('lavender', 'lavender'), ('blue', 'blue')], max_length=200),
        ),
        migrations.AlterField(
            model_name='mono',
            name='image',
            field=models.ImageField(default='null', upload_to='images/'),
        ),
    ]
