from django.db import models
from django.db.models.functions import datetime

from address.models import Address
from customer.models import Customer
from discount.models import Discount
from product.models import Product, Option
from shop.models import Shop
from user.models import User


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip = models.GenericIPAddressField(null=True)
    total_product_price = models.IntegerField()
    total_discount_price = models.IntegerField()
    total_tax_price = models.IntegerField()
    total_product_discount_price = models.IntegerField()
    total_final_price = models.IntegerField()
    send_price = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)
    STATUS_CHOICES = (
        ('wait_for_pay', 'WaitForPay'),
        ('wait_for_try_pay', 'WaitForTryPay'),
        ('paid', 'Paid'),
        ('wait_for_sender', 'WaitForSender'),
        ('wait_for_delivery', 'WaitForDelivery'),
        ('delivered', 'Delivered'),
        ('returned_timeout', 'ReturnedTimeout'),
        ('wait_for_accept_returned', 'WaitForAcceptReturned'),
        ('reject_returned', 'RejectReturned'),
        ('wait_for_sender_returned', 'WaitForSenderReturned'),
        ('delivered_returned', 'DeliveredReturned'),
        ('wait_for_returned_pay_back', 'WaitForReturnedPayBack'),
        ('returned_paid', 'ReturnedPaid')
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='wait_for_pay')
    description = models.TextField(null=True)
    package_size = models.CharField(max_length=255, null=True)
    tracking_code = models.CharField(max_length=255, null=True)
    courier = models.CharField(max_length=255, null=True)
    last_update_status_at = models.DateTimeField(default=datetime.datetime.now)
    weight = models.IntegerField(null=True)
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,related_name='orders')
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL,null=True,related_name='orders')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True,related_name='orders')
    discount_id = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True,related_name='orders')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True,related_name='orders')

    class Meta:
        db_table = "orders"

class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    count = models.IntegerField(default=1)
    quantity = models.IntegerField()  # موجودس محصول
    raw_price = models.IntegerField()  # قیمت اصلی محصول
    raw_price_option = models.IntegerField()  # قیمت اصلی اپشن
    raw_price_count = models.IntegerField()  # قیمت اصلی محصول با توجه به تعداد
    raw_price_option_count = models.IntegerField()  # قیمت اصلی اپشن با توجه به تعداد
    amount = models.IntegerField()  # قیمت تخفیف
    percent = models.IntegerField()  # درصد تخفیف
    off_price = models.IntegerField()  # قیمت تخفیف داده شده
    off_price_option = models.IntegerField()  # قیمت تخفیف داده شده اپشن
    new_price = models.IntegerField()  # قیمت به همراه تعداد و تخفیف
    new_price_option = models.IntegerField()  # قیمت به همراه تعداد و تخفیف اپشن
    final_raw_price = models.IntegerField()  # قیمت نهایی بدون تخفیف
    final_price = models.IntegerField()  # قیمت نهایی با تخفیف
    has_option = models.BooleanField()  # آیا این محصول اپشن دارد؟
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='order_items')
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True, related_name='order_items')


    class Meta:
        db_table = "order_items"