# Generated by Django 4.0.4 on 2022-05-10 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NShCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_id', models.BigIntegerField(blank=True, null=True)),
                ('n_quantity', models.IntegerField(blank=True, null=True)),
                ('n_item_id', models.BigIntegerField(blank=True, null=True)),
                ('users_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'n_sh_cart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CardInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.BigIntegerField()),
                ('expiry_date', models.DateField()),
                ('cvv', models.IntegerField()),
                ('is_default', models.BooleanField(blank=True, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ct_category_name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, verbose_name='URL')),
                ('c_count', models.IntegerField(blank=True, null=True, verbose_name='count')),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('address_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('street1', models.CharField(max_length=255)),
                ('street2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('is_default', models.BooleanField(blank=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='discProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.ImageField(upload_to='')),
                ('nob_disc_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('disc_price', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_title', models.CharField(max_length=255, verbose_name='Title')),
                ('p_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('slug', models.SlugField(max_length=255, verbose_name='URL')),
                ('p_description', models.TextField(blank=True, verbose_name='Product description')),
                ('p_photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Product photo')),
                ('p_time_create', models.DateTimeField(auto_now_add=True)),
                ('p_time_update', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('p_color', models.CharField(max_length=255, verbose_name='Display')),
                ('p_year', models.DateField(blank=True, null=True)),
                ('p_capacity', models.IntegerField(blank=True, null=True, verbose_name='Capacity')),
                ('p_display', models.CharField(blank=True, max_length=255, null=True, verbose_name='Display')),
                ('p_model_processor', models.CharField(blank=True, max_length=255, null=True, verbose_name='Model Processor')),
                ('p_weight', models.IntegerField(blank=True, null=True, verbose_name='Weight')),
                ('p_charge', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('p_batery_capacity', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('p_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Type')),
                ('p_fabric', models.CharField(blank=True, max_length=255, null=True, verbose_name='Material')),
                ('p_interfase', models.CharField(blank=True, max_length=255, null=True, verbose_name='Interface')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='count')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='poll.category')),
                ('users_wishlist', models.ManyToManyField(blank=True, related_name='user_wishlist', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-p_time_create',),
            },
        ),
        migrations.CreateModel(
            name='ProductShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shortsupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_p_title', models.CharField(blank=True, max_length=255, null=True)),
                ('s_count', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='poll.productshoppingcart')),
                ('s_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('shipping_price', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('order_status', models.CharField(max_length=1)),
                ('quantity', models.BigIntegerField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.cardinfo')),
                ('delivery_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.contactdetail')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.product')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='poll.product')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]