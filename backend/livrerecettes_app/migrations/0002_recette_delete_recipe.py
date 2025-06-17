from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livrerecettes_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('temps_preparation', models.IntegerField()),
                ('temps_cuisson', models.IntegerField()),
                ('portions', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]
