from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('inventory_recommendation', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('description', models.TextField()),
                ('farmer_contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='resource',
            name='crop',
        ),
        migrations.DeleteModel(
            name='Crop',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
        migrations.DeleteModel(
            name='SoilCondition',
        ),
        migrations.DeleteModel(
            name='Weather',
        ),
    ]