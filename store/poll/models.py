from operator import mod
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.



class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey('CardInfo', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    tax = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    shipping_price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    delivery_address = models.ForeignKey('ContactDetail', on_delete=models.CASCADE, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    order_status = models.CharField(max_length=1)
    quantity = models.BigIntegerField()
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    



    


class CardInfo(models.Model):
    card_number = models.BigIntegerField()
    expiry_date = models.DateField()
    cvv = models.IntegerField()
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    is_default = models.BooleanField(blank=True, null=True)


class NShCart(models.Model):
    n_id = models.BigIntegerField(blank=True, null=True)
    n_quantity = models.IntegerField(blank=True, null=True)
    n_item_id = models.BigIntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'n_sh_cart'
    




    
class ContactDetail(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_id = models.BigIntegerField(primary_key=True)
    street1 = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    phone = models.CharField(max_length=20)
    is_default = models.BooleanField(blank=True, null=True)

    












    

    


# class ShoppingCart(models.Model):
#     buyer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#     product_id = models.OneToOneField('Product', on_delete=models.CASCADE, primary_key=True)
#     date_added = models.DateField(blank=True, null=True)


# //////////////////////////////////////////////

class ProductShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    

    def __str__(self):
        return f"{self.quantity} of {self.item.p_title}"

    
    
    def get_total_item_price(self):
        return self.quantity * self.item.p_price

    

    def get_final_price(self):
        # if self.item.discount_price:
        #     return self.get_total_discount_item_price()
        return self.get_total_item_price()


class ShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    s_item = models.ForeignKey('Product', on_delete=models.CASCADE)
    items = models.ManyToManyField(ProductShoppingCart)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for cart_item in self.items.all():
            total += cart_item.get_total_item_price()
        return total
# ////////////////////////////////////////////
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Product(models.Model):
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    p_title = models.CharField(max_length=255, verbose_name="Title")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    p_price = models.DecimalField(max_digits=9, decimal_places=2)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")
    p_description = models.TextField(blank=True, verbose_name="Product description")
    p_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Product photo')
    p_time_create = models.DateTimeField(auto_now_add=True)
    p_time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete = models.PROTECT)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    # mac, watch, iphone
    p_color =  models.CharField(max_length=255, verbose_name="Display")
    p_year = models.DateField(blank=True, null=True)
    p_capacity = models.IntegerField(blank=True, null=True, verbose_name="Capacity")
    p_display = models.CharField(blank=True, null=True, max_length=255, verbose_name="Display")
    p_model_processor = models.CharField(blank=True, null=True, max_length=255, verbose_name="Model Processor")
    p_weight = models.IntegerField(blank=True, null=True, verbose_name="Weight")
    p_charge = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    p_diogonal = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True),
    p_batery_capacity = models.DecimalField(decimal_places=2,max_digits = 10, blank=True, null=True)
    # watch and pencil
    p_type = models.CharField(blank=True, null=True, max_length=255, verbose_name="Type")
    p_fabric =  models.CharField(blank=True, null=True, max_length=255, verbose_name="Material")
    p_interfase = models.CharField(blank=True, null=True, max_length=255, verbose_name="Interface")
    
    users_wishlist = models.ManyToManyField(User, related_name="user_wishlist", blank=True)
    
    count = models.IntegerField(blank=True, null=True, verbose_name="count")
    objects = models.Manager()
    published = PublishedManager()
    
    
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})
    # def get_absolute_url(self):
    #     return reverse("product-detail", kwargs={"pk": self.pk})
    

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })
    def get_add_to_wish_url(self):
        return reverse("user_wishlist", kwargs={
            'slug': self.slug
        })


   

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={"post_name": self.p_title})

    class Meta:
        ordering = ('-p_time_create',)

    def __str__(self):
        return self.p_title

    
    
class Category(models.Model):
    ct_category_name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")
    c_count = models.IntegerField(blank=True, null=True, verbose_name="count")


        
    def __str__(self):
        return self.ct_category_name
        
    
    def get_absolute_url(self):
        return reverse('category', kwargs={"cat_id": self.pk})



class Comment(models.Model):
    product = models.ForeignKey(Product,
                             on_delete=models.CASCADE,
                             related_name='comments',)
    # name = models.CharField(max_length=80)
    # email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


class discProduct(models.Model):
    p_id = models.ImageField()
    nob_disc_price = models.DecimalField(max_digits=9, decimal_places=2)
    disc_price = models.DecimalField(max_digits=9, decimal_places=2)



class Shortsupply(models.Model):
    s_p_title = models.CharField(max_length=255, blank=True, null=True)
    s_count = models.IntegerField(blank=True, null=True)

    