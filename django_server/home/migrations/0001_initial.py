# Generated by Django 4.1.4 on 2022-12-14 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('item_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('name', models.CharField(max_length=50)),
                ('status', models.IntegerField(choices=[(0, 'Available'), (1, 'Unavailable')])),
                ('image', models.FileField(upload_to='images/fooditems/')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('order_status', models.IntegerField(choices=[(0, 'New'), (1, 'Processing'), (2, 'ReadyToServe'), (3, 'Complete'), (-1, 'Cancelled')])),
                ('notes', models.CharField(max_length=100)),
                ('order_date_time', models.DateTimeField()),
                ('delivery_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=10)),
                ('shop_name', models.CharField(max_length=20)),
                ('shop_description', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images/shops/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('user_role', models.IntegerField(choices=[(0, 'Student'), (1, 'ShopAdmin')])),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.user')),
                ('password_hash', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('status', models.CharField(default='Pending', max_length=254, verbose_name='Payment Status')),
                ('provider_order_id', models.CharField(max_length=40, verbose_name='Order ID')),
                ('payment_id', models.CharField(max_length=36, verbose_name='Payment ID')),
                ('signature_id', models.CharField(max_length=128, verbose_name='Signature ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
        migrations.CreateModel(
            name='Owns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.shop')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_count', models.IntegerField()),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.fooditem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.shop'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
        migrations.CreateModel(
            name='OffDays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.shop')),
            ],
        ),
        migrations.AddField(
            model_name='fooditem',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.shop'),
        ),
    ]
