# Generated by Django 3.2.6 on 2021-08-22 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=20)),
                ('subcategory', models.CharField(max_length=50)),
                ('rental_price', models.IntegerField()),
                ('about', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('deposit', models.IntegerField()),
                ('seller_of_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_of_item', to='User.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Rent_Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivered_date', models.DateField()),
                ('sent_date', models.DateField()),
                ('payment', models.IntegerField()),
                ('satisfaction', models.BooleanField(default=True)),
                ('expected', models.DateField()),
                ('customer_of_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_of_item', to=settings.AUTH_USER_MODEL)),
                ('related_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rented_product', to='Rent.product')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review', models.TextField()),
                ('rating_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_by', to=settings.AUTH_USER_MODEL)),
                ('rating_for_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_for_product', to='Rent.product')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='product_photos')),
                ('product_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_name', to='Rent.product')),
            ],
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.TextField()),
                ('resolved', models.BooleanField(default=False)),
                ('complain_against', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complain_against', to='Rent.product')),
                ('complainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complainer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('confirmation', models.BooleanField()),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Rent.product')),
                ('customer_who_booked', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
