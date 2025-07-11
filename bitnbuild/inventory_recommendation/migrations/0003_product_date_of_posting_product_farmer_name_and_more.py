from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):
    dependencies = [
        ('inventory_recommendation', '0002_product_remove_resource_crop_delete_crop_and_more'),
    ]
    operations = [
        migrations.AddField(
            model_name='product',
            name='date_of_posting',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='farmer_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]