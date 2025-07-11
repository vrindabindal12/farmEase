from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('planting_timings', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SoilCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_recommendation.crop')),
            ],
        ),
        migrations.AddField(
            model_name='crop',
            name='optimal_soil_condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_recommendation.soilcondition'),
        ),
        migrations.AddField(
            model_name='crop',
            name='optimal_weather',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_recommendation.weather'),
        ),
    ]