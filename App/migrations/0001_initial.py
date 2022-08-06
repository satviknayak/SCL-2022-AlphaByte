# Generated by Django 4.0.6 on 2022-08-05 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, unique=True)),
                ('subscription_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('subscription_date', models.DateTimeField(blank=True, null=True)),
                ('subscription_end', models.DateTimeField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Waste',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True)),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('pickup_date', models.DateField(blank=True, null=True)),
                ('dropdown_date', models.DateField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('type', models.CharField(choices=[('STEEL', 'Steel'), ('BIO-DEGRADABLE', 'Bio-Degradable'), ('PAPER', 'Paper'), ('E-WASTE', 'E-Waste')], max_length=50, verbose_name='Types')),
                ('pickup_done', models.BooleanField(default=False)),
                ('dropdown_done', models.BooleanField(default=False)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to=settings.AUTH_USER_MODEL)),
                ('recycler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recycler', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(default='avatar.png', upload_to='Profile')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('street', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
